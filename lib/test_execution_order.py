from robot.api import ExecutionResult, ResultVisitor
from robot.utils import timestamp_to_secs as ts, secs_to_timestamp as st

res = ExecutionResult('output.xml')

class SuiteAndTestTimes(ResultVisitor):

    def __init__(self):
        self.result_by_start_time = []
        self.result_by_end_time = []
        self.suite_names = set()

    def visit_test(self, test):
        self.suite_names.add(test.parent.longname)
        self.result_by_start_time.append([ts(test.starttime), test.parent.longname, test.longname])
        self.result_by_end_time.append([ts(test.endtime), test.parent.longname, test.longname])

test_times = SuiteAndTestTimes()
res.visit(test_times)

result_by_start_time = sorted(test_times.result_by_start_time)
result_by_end_time = sorted(test_times.result_by_end_time)

starting, result_by_start_time = result_by_start_time[0], result_by_start_time[1:]
ending, result_by_end_time = result_by_end_time[0], result_by_end_time[1:]
currenttime = starting[0]

running = set()

while result_by_start_time or result_by_end_time:
    row = st(currenttime, millis=True)
    new_runners = set()
    runners_to_remove = set()
    while starting and starting[0] == currenttime:
        new_runners.add(starting[2])
        if result_by_start_time:
           starting, result_by_start_time = result_by_start_time[0], result_by_start_time[1:]
        else:
           starting = None
           break
    while ending and ending[0] == currenttime:
        runners_to_remove.add(ending[2])
        if result_by_end_time:
           ending, result_by_end_time = result_by_end_time[0], result_by_end_time[1:]
        else:
           ending = None
           break
    running -= runners_to_remove
    row += ' [RUN] "%s"' % '" "'.join(sorted(running)) if running else ''
    row += ' [START] "%s"' % '" "'.join(sorted(new_runners)) if new_runners else ''
    row += ' [END] "%s"' % '" "'.join(sorted(runners_to_remove)) if runners_to_remove else ''
    running |= new_runners
    print row
    if starting and ending:
        currenttime = min(starting[0], ending[0])
    elif starting:
        currenttime = starting[0]
    elif ending:
        currenttime = ending[0]
if ending:
    print '%s [END] "%s"' % (st(ending[0], millis=True), ending[2])