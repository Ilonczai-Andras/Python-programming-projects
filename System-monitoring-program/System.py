import psutil
import time
import sys
import datetime

VERSION = "v1.0.0"
CREATOR = "Ilonczai András"

def this_day():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()  # Get the current date

    result = "" + str(current_date)
    return result

def file_name():
    return "log_" + this_day()+ "_.txt"

def monitor_system(duration, log_file):
    start_time = time.time()
    end_time = start_time + duration

    with open(log_file, 'a') as file:
            file.write("\n")

    while time.time() < end_time:

        #Rendszer információk
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        # Naplózás a fájlba
        log_data = f"Date_Time: {time.ctime()}, CPU usage: {cpu_usage}%, Memory usage: {memory_usage}%, Disk usage: {disk_usage}%\n"
        with open(log_file, 'a') as file:
            file.write(log_data)

        time.sleep(0.1)
def alap():
    print(f"Creator: {CREATOR}\n")
    print(f"Monitor System {VERSION}\n")
    print("Available options: ")
    print("-creator                            show creator")
    print("-h,  -help                          show this help")
    print("-v,  --version                      version info")
    print("-make_data,                         start generating data from this moment. Interval = 0.1 || Duration = 3600")
    print("-make_data duration                 same as above, but u can configure the duration(count)")
    print("-stdout,                            print the Usages at this moment")

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python script.py ...")
        sys.exit(1)
    else:
        
        if(sys.argv[1] == "alap" or sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            alap()

        elif(sys.argv[1] == "-v" or sys.argv[1] == "--version"):
            print(f"{VERSION}")

        elif(sys.argv[1] == "-creator"):
            print(f"{CREATOR}")

        elif len(sys.argv) == 3:
            if(sys.argv[1] == "-make_data" and isinstance(float(sys.argv[2]), float) ):

                monitor_system(int(sys.argv[2]), file_name())

        elif len(sys.argv) == 2:
            if(sys.argv[1] == "-make_data"):
                monitor_system(3600, file_name())

            elif(sys.argv[1] == "-stdout"):
                cpu_usage = psutil.cpu_percent(interval=1)
                memory_usage = psutil.virtual_memory().percent
                disk_usage = psutil.disk_usage('/').percent
                print(f"\nDate_Time: {time.ctime()}, CPU usage: {cpu_usage}%, Memory usage: {memory_usage}%, Disk usage: {disk_usage}%\n")
        else:
            print("Wrong argumets!")