class Printter(object):
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self._main_suite = True
        self.passed_all = 0
        self.failed_all = 0
        self.passed_critical = 0
        self.failed_critical = 0

    def start_suite(self, name, attributes):
        if not self._main_suite:
            return
        self._main_suite = False
        self._total = attributes['totaltests']

    def end_test(self, name, attributes):
        self._update_status(attributes)
        self._print_status()

    def _update_status(self, attributes):
        if attributes['critical'] == 'yes':
            if attributes['status'] == 'PASS':
                self.passed_critical += 1
            else:
                self.failed_critical += 1
        if attributes['status'] == 'PASS':
            self.passed_all += 1
        else:
            self.failed_all += 1

    def _print_status(self):
        print '='*78
        print 'CRITICAL passed %d failed %d total %d' % (self.passed_critical, self.failed_critical, self.passed_critical+self.failed_critical)
        print 'ALL      passed %d failed %d total %d / %d' % (self.passed_all, self.failed_all, self.passed_all+self.failed_all, self._total)
        print '='*78