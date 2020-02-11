class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month == 1 or month == 2:
            month += 12
            year -= 1
        weeks = (day + 2*month + (3*(month + 1))//5 + year + year//4 - year//100 + year//400)% 7
        dic = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return dic[weeks]