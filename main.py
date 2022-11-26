import psutil
import time
import MacTmp


class SysMonitor:
    def __init__(self, period=5):
        self.period = period

    def memory(self):
        """
        Getting system memory stats
        """
        print('Memory usage: ', psutil.virtual_memory()[2], '%')

    def cpu(self):
        """
        Getting system CPU stats
        """
        print('System CPU percentage: ', psutil.cpu_percent(), '%')
        print('CPU percentage per core: ', psutil.cpu_percent(percpu=True))

    def loadavg(self):
        """
        Gets the system load average
        """
        print('Load average: ', psutil.getloadavg())

    def temperature(self):
        """
        Gets the CPU temperature
        """
        # print('CPU temperature: ', psutil.sensors_temperatures()) for Linux and FreeBSD only
        print('CPU temperature: ', MacTmp.CPU_Temp(), 'C')

    def battery(self):
        """
        Getting battery status
        """
        print('Battery status: ', psutil.sensors_battery())

    def disk_util(self):
        """
        Disk usage information
        """
        print('Disk usage: ', psutil.disk_usage('/dev/disk1s5'))

    def process_monitor(self):
        """
        Gets a process listing showing the cpu usage
        """
        print('Process Listing: ')
        for process in psutil.process_iter():
            process_info = process.as_dict(attrs=['name', 'cpu_percent'])
            if process_info['cpu_percent'] and process_info['cpu_percent'] > 10:
                print(process_info)


if __name__ == '__main__':
    repeat = 0
    a = SysMonitor()
    while True:
        repeat += 1
        print(f'\nRepeat #{repeat}, {a.period} seconds timeout \n')
        a.memory()
        a.cpu()
        a.loadavg()
        a.temperature()
        #a.battery()
        #a.disk_util()
        a.process_monitor()
        time.sleep(a.period)
        