import create_db
import re


def main():
    pattern = re.compile("^consume --count [0-9]$")

    create_db.create()

    print ("Make your selection")
    print ("consume --count n | show | clear: ")
    input1 = input()

    if input1 == "clear":
        import clear_db
        clear_db.clear()

    elif input1 == "show":
        import show
        show.show()

    elif pattern.match(input1):
        out = input1.split(" ")
        import consumer
        consumer.consumer(int(out[2]))

    else:
        print("Wrong Output. Exiting!")
        exit

if __name__ == "__main__":
    main()