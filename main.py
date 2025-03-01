import race_condition
import deadlock
import producer_consumer
import reader_writer
import dinning_philosopher
import priority_inversion
import bounded_buffer

def show_menu():
    print("Choose an example to run:")
    print("1. Race Condition Example")
    print("2. Deadlock Example")
    print("3. Producer-Consumer Example")
    print("4. Reader-Writer Example")
    print("5. Dining Philosophers Example")
    print("6. Priority Inversion Example")
    print("7. Bounded Buffer Example")
    print("8. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            print("\nRace Condition Example")
            race_condition.race_condition_example()
        elif choice == "2":
            print("\nDeadlock Example")
            deadlock.deadlock_example()
        elif choice == "3":
            print("\nProducer-Consumer Example")
            producer_consumer.producer_consumer_example()
        elif choice == "4":
            print("\nReader-Writer Example")
            reader_writer.reader_writer_example()
        elif choice == "5":
            print("\nDining Philosophers Example")
            dinning_philosopher.dining_philosophers_example()
        elif choice == "6":
            print("\nPriority Inversion Example")
            priority_inversion.priority_inversion_example()
        elif choice == "7":
            print("\nBounded Buffer Example")
            bounded_buffer.bounded_buffer_example()
        elif choice == "8":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
