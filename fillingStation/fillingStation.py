# There is a queue of N cars waiting at a filling station. There are three fuel dispensers at the station, labeled X, Y and Z, respectively. Each dispenser has some finite amount of fuel in it; at all times the amount of available fuel is clearly displayed on each dispenser.

# When a car arrives at the front of the queue, the driver can choose to drive to any dispenser not occupied by another car. Suppose that the fuel demand is D liters for this car. The driver must choose a dispenser which has at least D liters of fuel. If all unoccupied dispensers have less than D liters, the driver must wait for some other car to finish tanking up. If all dispensers are unoccupied, and none has at least D liters, the driver is unable to refuel the car and it blocks the queue indefinitely. If more than one unoccupied dispenser has at least D liters, the driver chooses the one labeled with the smallest letter among them.

# Each driver will have to wait some amount of time before he or she starts refueling the car. Calculate the maximum waiting time among all drivers. Assume that tanking one liter of fuel takes exactly one second, and moving cars is instantaneous.

# Write a function:

# def solution(A, X, Y, Z)

# that, given an array A consisting of N integers (which specify the fuel demands in liters for subsequent cars in the queue), and numbers X, Y and Z (which specify the initial amount of fuel in the respective dispensers), returns the maximum waiting time for a car. If any car is unable to refuel, the function should return −1.

# For example, given X = 7, Y = 11, Z = 3 and the following array A:

#     A[0] = 2
#     A[1] = 8
#     A[2] = 4
#     A[3] = 3
#     A[4] = 2
# the function should return 8. The subsequent cars will have to wait in the queue for 0, 0, 2, 2 and 8 seconds, respectively. The scenario is as follows:

# At time 0, car 0 drives to dispenser X.
# At time 0, car 1 drives to dispenser Y.
# There is not enough fuel in dispenser Z to satisfy the demands of car 2, so this car must wait. At time 2 car 0 finishes refueling and car 2 drives to dispenser X.
# At time 2 car 3 drives to dispenser Z.
# At this time all dispensers are occupied, so car 4 waits. There will be not enough fuel in dispensers X and Z after cars 2 and 3 finish tanking up, so car 4 waits until car 1 finishes refuelling at dispenser Y. At time 8, car 4 drives to dispenser Y.
# For X = 4, Y = 0, Z = 3 and array A:

#     A[0] = 5
# the function should return −1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# X, Y and Z are integers within the range [0..1,000,000,000].
class Dispensers:
    def __init__(self, x, y, z):
        self._free = [x, y ,z]
        self._busy = [False, False, False]

    def free(self, idx):
        self._busy[idx] = False
    
    def consume(self, idx, demand):
        self._free[idx] = self._free[idx] - demand

    def busy(self, idx):
        self._busy[idx] = True

    def get(self, demand):
        for idx, dispenser in enumerate(self._free):
            if dispenser >= demand and not self._busy[idx]:
                return idx

        return -1

WORK_PER_SEC = 1
class Scheduler:
    def __init__(self, cars, dispensers):
        self._wait = 0
        self._cars = cars
        self._dispensers = dispensers
        self._works = [] ## [[dispenserID, workload]]

    def wait(self, time):
        self._wait += time

    def working(self, car, idx):
        self._dispensers.busy(idx)
        self._works.append([idx, car])
        self._cars.pop(0)

    def excute(self):
        if len(self._works) == 0:
            return -1
        time = 0 ## excuting time of the minimal works
        while True:
            hasFreed = False

            currentWorks = self._works.copy()
            for idx, work in enumerate(currentWorks):
                if currentWorks[idx][1] == 0: ## complete work
                    self._dispensers.free(currentWorks[idx][0])
                    self._works.remove(work)
                    hasFreed = True


            if hasFreed:
                break
            
            for idx, work in enumerate(self._works): ## consume dispenser and excute work
                work[1] -= 1
                self._dispensers.consume(work[0], 1)
            time += 1

        # self._wait += time
        return time

    def work_loop(self):
        while True:
            if len(self._cars) == 0:
                break

            car = self._cars[0]

            dispenser = self._dispensers.get(car)

            if dispenser != -1:
                self.working(car, dispenser)
            else: ## wait to works
                duration = self.excute()
                self._wait += duration
                if duration == -1 and self._wait == 0:
                    self._wait = -1
                
    def get_wait(self):
        return self._wait

def solution(A, X, Y, Z):
    schl = Scheduler(A, Dispensers(X, Y, Z))
    schl.work_loop()
    return schl.get_wait()

print(solution([2,8,4,3,2], 7, 11, 3))