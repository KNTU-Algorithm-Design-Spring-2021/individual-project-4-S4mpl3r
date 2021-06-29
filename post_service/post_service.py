from queue import PriorityQueue


class Package:
    def __init__(self, number, weight):
        self.number = number
        self.weight = weight

    def __str__(self) -> str:
        return f"<{self.number}: {self.weight}kg>"


class Truck:
    def __init__(self, number):
        self.number = number
        self.packageList = []

    def __lt__(self, o):
        return self.calculateWeight() < o.calculateWeight()

    def __eq__(self, o):
        return self.calculateWeight() == o.calculateWeight()

    def __str__(self) -> str:
        tmp, sum = [], 0
        for item in self.packageList:
            tmp.append((item.number, str(item.weight) + "kg"))
            sum += item.weight
        return f"truck {self.number} => {tmp} => {sum}kg"

    def addPackage(self, package):
        self.packageList.append(package)

    def calculateWeight(self):
        sum = 0
        for item in self.packageList:
            sum += item.weight
        return sum


class PostService:
    def __init__(self, numberOfTrucks, numberOfPackages):
        self.numberOfTrucks = numberOfTrucks
        self.numberOfPackages = numberOfPackages
        self.trucks = PriorityQueue()
        self.packages = []

    def initTrucksAndPackages(self):
        for i in range(1, self.numberOfTrucks+1):
            truck = Truck(i)
            self.trucks.put(truck)
        tmp = [int(x) for x in input().split(' ')[:self.numberOfPackages]]
        for i in range(1, self.numberOfPackages+1):
            self.packages.append(Package(i, tmp[i-1]))

    def printTrucksAndPackages(self):
        trucks = []
        for _ in range(self.trucks.qsize()):
            truck = self.trucks.get()
            trucks.append(truck)
            print(truck)
        for truck in trucks:
            self.trucks.put(truck)
        print("Packages:")
        for package in self.packages:
            print(package)

    def applyGreedyDistribution(self):
        for item in self.packages:
            truck = self.trucks.get()
            truck.addPackage(item)
            self.trucks.put(truck)


def main():
    N, K = [int(x) for x in input(
        "Enter number of packages and trucks: ").split(' ')[:2]]
    print("Enter package weights: ")
    postService = PostService(K, N)
    postService.initTrucksAndPackages()
    postService.applyGreedyDistribution()
    print("---------------------------")
    postService.printTrucksAndPackages()


if __name__ == "__main__":
    main()
