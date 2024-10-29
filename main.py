import os,subprocess
def memory_stress_test():
    print("Starting Memory Stress Test...")
    # Running memory stress test with stress-ng
    #subprocess.run(['stress-ng', '--vm', '2', '--vm-bytes', '80%'])
    os.system("stress-ng --vm 1 --vm-bytes 80% -t 30s ")
    print("Memory Stress Test Completed.")

def disk_stress_test():
    print("Starting Disk Stress Test...")
    # Running disk stress test with stress-ng
    #subprocess.run(['stress-ng', '--hdd', '2', '--hdd-bytes', '80%'])
    #os.system("stress-ng --iomix 4 --iomix-bytes 80% --timeout 30s ")
    os.system("stress-ng --hdd 2 --hdd-bytes 80% --timeout 30s ")
    print("Disk Stress Test Completed.")

def network_stress_test():
    print("Starting Network Stress Test...")
    '''# Assuming iperf3 server is running on vm_2 with IP 192.168.29.49
    #result = subprocess.run(['iperf3', '-c', '192.168.1.2', '-t', '10'], capture_output=True, text=True)
    #print(result.stdout)
    os.system("stress-ng --net 4 --net-bytes  80M --timeout 30s")'''
    print("Network Stress Test Completed.")

def cpu_stress_test():
    print("Starting CPU Stress Test...")
    # Running CPU stress test with stress-ng
    #subprocess.run(['stress-ng', '--cpu', '2', '--timeout', '60'])
    os.system("stress-ng --cpu 4 --cpu-load 80 -t 30s")
    print("CPU Stress Test Completed.")

def mysql_stress_test():
    # Running sysbench for MySQL stress testing
    # Adjust the parameters as needed
    print("Starting MySQL Stress Test...")
    '''process = subprocess.Popen([
        'sysbench',
        '--test=/usr/share/sysbench/oltp_read_only.lua',
        '--mysql-db=test',
        '--mysql-user=root',
        '--mysql-password=',
        '--max-time=30',
        '--max-requests=0',
        '--threads=2',
        'run'
    ])
    #return process'''
    print("MySQL Stress Test Completed.")


def main():
    while True:
        print("\nSelect an option for stress testing:")
        print("1. Memory Stress Testing")
        print("2. Disk Stress Testing")
        print("3. Network Stress Testing")
        print("4. CPU Stress Testing")
        print("5. MySQL Stress Testing")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            memory_stress_test()
        elif choice == 2:
            disk_stress_test()
        elif choice == 3:
            network_stress_test()
        elif choice == 4:
            cpu_stress_test()
        elif choice == 5:
            mysql_stress_test()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()