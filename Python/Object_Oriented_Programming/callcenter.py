from operator import itemgetter, attrgetter
import time
class Call(object):
    def __init__(self, unique_id, caller_name, caller_tel, call_time, call_reason):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_tel = caller_tel
        self.call_time = call_time
        self.call_reason = call_reason
    def displayInfo(self):
        print "Id:", self.unique_id
        print "Caller Name:", self.caller_name
        print "Call Phone Number:", self.caller_tel
        print "Time of Call:", self.call_time
        print "Reason for Call:", self.call_reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def addCall(self, unique_id, caller_name, caller_tel, call_time, call_reason):
        call = Call(unique_id, caller_name, caller_tel, call_time, call_reason)
        self.calls.append(call)
        self.queue_size += 1
        return self
    def removeCall(self):
        self.calls.remove(self.calls[0])
        self.queue_size -= 1
        return self
    def info(self):
        for call in self.calls:
            print "Name:", call.caller_name
            print "Caller Phone Number:", call.caller_tel
            print "Call Time:", call.call_time
        print "Queue Size:", self.queue_size
        return self
    def findAndRemove(self, caller_tel):
        for findcall in self.calls:
            if findcall.caller_tel == caller_tel:
                self.calls.remove(findcall)
                self.queue_size -= 1
        return self

call1 = Call(1225, "Helen Brown", "555-245-6789", 17:45, "late delivery")
call2 = Call(1432, "Michael Adams", "555-756-2309", 07:08, "damaged goods")
call3 = Call(1356, "Jasmin Ortiz", "555-984-0988", 14:31, "billing issues")
call4 = Call(1458, "Melanie Newby", "555-987-3849", 09:25, "late delivery")
callcenter1 = CallCenter()
callcenter1.addCall(1225, "Helen Brown", "555-245-6789", 17:45, "late delivery").addCall(1432, "Michael Adams", "555-756-2309", 07:08, "damaged goods").addCall(1356, "Jasmin Ortiz", "555-984-0988", 14:31, "billing issues")
callcenter1.removeCall()
callcenter1.info()
callcenter1.findAndRemove("555-756-2309")
callcenter1.info()
