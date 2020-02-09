"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0
        subrelation = dict()
        for emp in employees:
            subrelation[emp.id] = [emp.importance, emp.subordinates]

        sub = [id]
        sum_import = 0
        while sub:
            emp_id = sub.pop(0)
            emp = subrelation[emp_id]
            sum_import += emp[0]
            if not emp[1]:
                continue
            for s in emp[1]:
                sub.append(s)

        return sum_import
