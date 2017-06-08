students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# Part 1
def names(arr):
    for i in range(0, len(arr)):
        for val in arr[i].itervalues():
            print val,
        print "\t"

names(students)

#Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def names2(dict):
    print 'Students'
    i = 0
    for x in dict['Students']:
        i += 1
        print i, "-", x['first_name'].upper(), x['last_name'].upper(), "-", len(x['first_name'] + x['last_name'])
    i = 0
    print 'Instructors'
    for x in dict['Instructors']:
        i += 1
        print i, "-", x['first_name'].upper(), x['last_name'].upper(), "-", len(x['first_name'] + x['last_name'])

names2(users)
