import datetime

class Solution:
    def daysBetweenDates(self, date1, date2):
        d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        d = d1 - d2
        print(abs(d.days))
        return abs(d.days)


s = Solution()
date1 = "2019-06-29"
date2 = "2019-06-30"
s.daysBetweenDates(date1, date2)