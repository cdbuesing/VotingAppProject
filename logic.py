
def submit(self):
    """
    Verifies the provided ID is valid and unused, then checks that a candidate has been selected, then records the vote

    Returns:
        nothing
    """
    voter_id = self.getId()
    voter_id = voter_id.strip()
    if(id_check(voter_id) == False):
        self.setMessage("Invalid ID", "red")
        return
    voter_id = int(voter_id)
    if(votefile_check()):
        votes_file = open('votes.txt', 'r')
        vote_lines = votes_file.read()
        vote_lines = vote_lines.split('\n')
        vote_lines.pop()
        for i in range(len(vote_lines)):
            cur_line = vote_lines[i].split(' ')
            if(int(cur_line[0]) == voter_id):
                self.setMessage("Already Voted", "red")
                votes_file.close()
                return
        votes_file.close()
    chosen_candidate = self.getVote()
    if(chosen_candidate == 'NA'):
        self.setMessage("Select A Candidate", "red")
        return
    votes_file = open('votes.txt', 'a')
    votes_file.write(f'{voter_id} voted {chosen_candidate}\n')
    votes_file.close()
    self.setMessage(f'Successfully Voted for {chosen_candidate}', "green")
    self.reset()

def id_check(temp_id):
    """
    Checks that the temp_id is an 8-digit number

    Args:
        temp_id (str): the id to be checked

    Returns:
        True if temp_id is an 8-digit number, False otherwise
    """
    while True:
        try:
            temp_id = int(temp_id)
            if(len(str(temp_id)) == 8):
                break
            return False
        except ValueError:
            return False
    return True

def votefile_check():
    """
    Checks that the votes.txt file exists

    Returns:
        True if the file exists and False if it does not
    """
    while True:
        try:
            with open('votes.txt', 'r') as f:
                break
        except FileNotFoundError:
            return False
    return True

def results(self):
    """
    Calls the update_results function, then changes the current page to the results page

    Returns:
        nothing
    """
    update_results(self)
    frame = self.getFrame(1)
    frame.tkraise()

def update_results(self):
    """
    Updates the vote results to match the current vote counts

    Returns:
        self
    """
    if(votefile_check()==False):
        return
    votes_file = open('votes.txt', 'r')
    vote_lines = votes_file.read()
    vote_lines = vote_lines.split('\n')
    vote_lines.pop()
    fred_count = 0
    george_count = 0
    bob_count = 0
    for i in range(len(vote_lines)):
        cur_line = vote_lines[i].split(' ')
        if(cur_line[2] == 'Fred'):
            fred_count += 1
        elif(cur_line[2] == 'George'):
            george_count += 1
        else:
            bob_count += 1
    self.setResults(f'Fred: {fred_count}  George: {george_count}  Bob: {bob_count}')