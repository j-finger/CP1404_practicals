from prac_08.taxi import Taxi

def main():
    taxi_1 = Taxi("Prius 1", 100, 1.23)
    taxi_1.drive(40)
    print(taxi_1)
    taxi_1.start_fare()
    print(taxi_1)


main()
