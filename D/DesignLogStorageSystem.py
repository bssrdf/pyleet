'''
-Medium-


You  are given several logs that each log contains a unique id and timestamp. Timestamp is a 
string that has the following format:Year:Month:Day:Hour:Minute:Second, for example,
2017:01:01:23:59:59. All domains are zero-padded decimal numbers.
Design a log storage system to implement the following functions:
void Put(int id, string timestamp): Given a log's unique id and time-stamp, store the log 
in your storage system.

int[] Retrieve(String start, String end, String granularity): Return the id of logs whose 
timestamps are within the range from start to end. Start and end all have the same format 
as timestamp. However, granularity means the time level for consideration. For example, 
start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means 
that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
Note:
There will be at most 300 operations of Put or Retrieve.
Year ranges from [2000,2017]. Hour ranges from [00,23].
Output for Retrieve has no order required.

'''
'''

The Idea: I think there are two key ideas to understand here. First, when logs are 
compared by granularity, we are only interested in the timestamps by their truncated form. 
For example,
"2016:01:01:01:01:01" by "Day" should yield
"2016:01:01"

This mean that a log id is valid if it falls in between the start and end times by its 
granularity. 

The second thing to understand is that string comparisons are valid forms of comparison in 
our case. This due to the nature of now the numbers are formatted as a date time. The time 
components are in ascending order, and within each component like year of day, a higher 
number implies that it occurs later. All of this to say that string comparison is a quick 
way to validity if a log time falls in between start and end.

Complexity: O(1) put operation, and O(n) retrieve operation

'''

class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.logs.append((id, timestamp))


    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        # index that maps up to the maximum granularity
        index = {'Year': 5, 'Month': 8, 'Day': 11, 
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]

        # slics all the way up till the granularity level
        start = s[:index]  
        end = e[:index]

        return [id for id, ts in self.logs if start <= ts[:index] <= end]

if __name__ == "__main__":
# Your LogSystem object will be instantiated and called as such:
   obj = LogSystem()
   obj.put(1, "2017:01:01:23:59:59")
   obj.put(2, "2017:01:01:22:59:59")
   obj.put(3, "2016:01:01:00:00:00")
   print(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year")) # return [1,2,3], because you need to return all logs within 2016 and 2017.
   print(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour")) # return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
 # obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)