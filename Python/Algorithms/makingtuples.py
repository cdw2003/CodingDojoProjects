my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dictIn_tuplesOut(dict):
    my_List = []
    for key,data in dict.iteritems():
        my_List.append((key,data))
    print my_List

dictIn_tuplesOut(my_dict)
