from collections import OrderedDict


class Timetable(OrderedDict):
    def __init__(self, name, fixedslots=False):
        self.name = name
        self.roomno = ''
        self.dept = ''
        self.final = OrderedDict()
        for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
            self[day] = OrderedDict({1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''})
            self.final[day] = OrderedDict(
                {1: fixedslots, 2: fixedslots, 3: fixedslots, 4: fixedslots, 5: fixedslots, 6: fixedslots,
                 7: fixedslots, 8: fixedslots})
        self['saturday'] = {1: '', 2: '', 3: '', 4: ''}
        self.final['saturday'] = OrderedDict({1: fixedslots, 2: fixedslots, 3: fixedslots, 4: fixedslots})
        self.workload = 0

    def calc_workload(self):
        workload = 0
        for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            for timeslot in self[day]:
                if self.final[day][timeslot] == True:
                    workload += 1
        self.workload += workload
        self.workload /= 44


faculty = {
    'Mr. Ajay Sharma': Timetable('Mr. Ajay Sharma'),
    'Mr. Ravi Kumar': Timetable('Mr. Ravi Kumar'),
    'Mr. Rajesh Patel': Timetable('Mr. Rajesh Patel'),
    'Mr. Suresh Menon': Timetable('Mr. Suresh Menon'),
    'Mr. Sanjay Gupta': Timetable('Mr. Sanjay Gupta'),
    'Mr. Roshan Mehta': Timetable('Mr. Roshan Mehta'),
    'Dr. Uday Kumar Singh': Timetable('Dr. Uday Kumar Singh'),
    'Mr. Raghav Verma': Timetable('Mr. Raghav Verma'),
    'Mrs. Shabana Sheikh': Timetable('Mrs. Shabana Sheikh'),
    'Mrs. Asmitha Roy': Timetable('Mrs. Asmitha Roy'),
    'Dr. Kiran Reddy': Timetable('Dr. Kiran Reddy'),
    'Mrs. Sharada Rao': Timetable('Mrs. Sharada Rao'),
    'Mr. Raju Nair': Timetable('Mr. Raju Nair'),
    'Mr. Ranjan Das': Timetable('Mr. Ranjan Das'),
    'Mrs. Pallavi Naik': Timetable('Mrs. Pallavi Naik'),
    'Mr. Ramesh Shetty': Timetable('Mr. Ramesh Shetty'),
    'Mr. Krishna Prasad': Timetable('Mr. Krishna Prasad'),
    'Mrs. Sarika Hegde': Timetable('Mrs. Sarika Hegde'),
    'Mrs. Savitha Nair': Timetable('Mrs. Savitha Nair'),
    'Dr. D K Sreekantha': Timetable('Dr. D K Sreekantha'),
    'Mrs. Jyothi Shetty': Timetable('Mrs. Jyothi Shetty'),
    'Mr. Sudeepa B': Timetable('Mr. Sudeepa B'),
    'Mr. Pradeep K': Timetable('Mr. Pradeep K'),
    'Mr. Vijay Murari': Timetable('Mr. Vijay Murari'),
    'Dr. Mohammed Javed': Timetable('Dr. Mohammed Javed'),
    'Mr. Chandra Naik': Timetable('Mr. Chandra Naik'),
    'Mrs. Anisha Rodrigues': Timetable('Mrs. Anisha Rodrigues'),
    'Mr. Raghunandan K R': Timetable('Mr. Raghunandan K R'),
    'Mrs. Minu Abraham': Timetable('Mrs. Minu Abraham'),
    'Mr. Sampath Kini': Timetable('Mr. Sampath Kini'),
    'Mr. Mahesh Kini': Timetable('Mr. Mahesh Kini'),
    'Mr. Manjunath Prasad': Timetable('Mr. Manjunath Prasad'),
    'Mr. Naveen Chandavarkar': Timetable('Mr. Naveen Chandavarkar'),
    'Mr. Pawan Hegde': Timetable('Mr. Pawan Hegde'),
    'Mrs. Keerthana B C': Timetable('Mrs. Keerthana B C'),
    'Mr. Sunil Aithal': Timetable('Mr. Sunil Aithal'),
    'Mr. Shashank Shetty': Timetable('Mr. Shashank Shetty'),
    'Mr. Puneeth R P': Timetable('Mr. Puneeth R P'),
    'Mrs. Shilpa M K': Timetable('Mrs. Shilpa M K'),
    "Mrs. Divya D'Souza": Timetable("Mrs. Divya D'Souza"),
    'Mrs. Rajalaxmi Hegde': Timetable('Mrs. Rajalaxmi Hegde'),
    'Mr. Sandeep Hegde': Timetable('Mr. Sandeep Hegde'),
    'Ms. Swathi Pai': Timetable('Ms. Swathi Pai'),
    'Ms. Ankitha Nayak': Timetable('Ms. Ankitha Nayak'),
    'Ms. Rajashree': Timetable('Ms. Rajashree'),

    # Maths
    'Ms. Smitha G V': Timetable('Ms. Smitha G V', fixedslots=True),
    'Dr. Shashirekha Rai': Timetable('Dr. Shashirekha Rai', fixedslots=True),
    'Ms. Anitha Bayar': Timetable('Ms. Anitha Bayar', fixedslots=True),
    "Ms. Apoorva D'Souza": Timetable("Ms. Apoorva D'Souza", fixedslots=True),

    # Humanities
    'Mr. Rama Krishna': Timetable('Mr. Rama Krishna'),
    'Humanities': Timetable('', fixedslots=True),

    '': Timetable('')
}

subjects = {
    'I BCA': (
        ('Fundamentals of Computers', 0, 'Mr. Ajay Sharma', 'Computer'),
        ('C Programming', 4, 'Mr. Ravi Kumar', 'Programming'),
        ('Data Structures and Algorithms', 4, 'Mr. Rajesh Patel', 'DSA'),
        ('Operating Systems', 4, 'Mr. Suresh Menon', 'OS'),
        ('Database Management Systems', 4, 'Mr. Sanjay Gupta', 'DBMS'),
        ('Software Engineering', 4, 'Mr. Roshan Mehta', 'SE'),
        ('Web Development', 4, 'Mrs. Shabana Sheikh', 'Web Dev'),
        ('Computer Networks', 4, 'Mr. Sudeepa B', 'CN'),
        ('Artificial Intelligence', 4, 'Mr. Pradeep K', 'AI'),
        ('Cloud Computing', 4, 'Mr. Vijay Murari', 'Cloud'),
    ),
    'II BCA': (
        ('Fundamentals of Computers', 0, 'Mr. Raghav Verma', 'Computer'),
        ('C Programming', 4, 'Mrs. Asmitha Roy', 'Programming'),
        ('Data Structures and Algorithms', 4, 'Dr. Kiran Reddy', 'DSA'),
        ('Operating Systems', 4, 'Mrs. Sharada Rao', 'OS'),
        ('Database Management Systems', 4, 'Mr. Raju Nair', 'DBMS'),
        ('Software Engineering', 4, 'Mr. Ranjan Das', 'SE'),
        ('Web Development', 4, 'Mrs. Pallavi Naik', 'Web Dev'),
        ('Computer Networks', 4, 'Mr. Ramesh Shetty', 'CN'),
        ('Artificial Intelligence', 4, 'Mr. Krishna Prasad', 'AI'),
        ('Cloud Computing', 4, 'Mrs. Sarika Hegde', 'Cloud'),
    ),
    'III BCA': (
        ('Fundamentals of Computers', 0, 'Mrs. Savitha Nair', 'Computer'),
        ('C Programming', 4, 'Dr. D K Sreekantha', 'Programming'),
        ('Data Structures and Algorithms', 4, 'Mrs. Jyothi Shetty', 'DSA'),
        ('Operating Systems', 4, 'Mr. Sudeepa B', 'OS'),
        ('Database Management Systems', 4, 'Mr. Pradeep K', 'DBMS'),
        ('Software Engineering', 4, 'Mr. Vijay Murari', 'SE'),
        ('Web Development', 4, 'Dr. Mohammed Javed', 'Web Dev'),
        ('Computer Networks', 4, 'Mr. Chandra Naik', 'CN'),
        ('Artificial Intelligence', 4, 'Mrs. Anisha Rodrigues', 'AI'),
        ('Cloud Computing', 4, 'Mr. Raghunandan K R', 'Cloud'),
    )
}
