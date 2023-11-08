import random
import time

def typing_speedtest():
    words= ['isaac','wonders','why','apple','fall','downwards','not','but','upwards']

    test_string=" ".join(random.choice(words) for _ in range(10))
    print("Type the following as fast as you can: ")
    print(test_string)
    input("Press Enter to start to the timer and Type when you are ready.....")
    start_time=time.time()
    userinput=input("Type the above given text: ")
    end_time=time.time()

    if userinput == test_string:
        time_taken=end_time - start_time
        wpm= len(test_string.split())/(time_taken/60)
        accuracy = calculate_accuracy(test_string, userinput)
        print(f"Time taken: {time_taken:.2f} seconds")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Your typing speed: {wpm:.2f} WPM (words per minute)")
    else:
        print("You made a mistake. Try Again ")
        accuracy = calculate_accuracy(test_string, userinput)
        print(f"Accuracy: {accuracy:.2f}%")
        time_taken=end_time - start_time
        print(f"Time taken: {time_taken:.2f} seconds")
        wpm= len(test_string.split())/(time_taken/60)
        print(f"Your typing speed: {wpm:.2f} WPM (words per minute)")

def calculate_accuracy(ref_text, typed_text):
    ref_text = ref_text.lower()  
    typed_text = typed_text.lower()
    
    ref_text = ' '.join(ref_text.split())
    typed_text = ' '.join(typed_text.split())
    
    min_len = min(len(ref_text), len(typed_text))
    
    correct_characters = sum(1 for r, t in zip(ref_text, typed_text) if r == t)
    accuracy = (correct_characters / min_len) * 100

    return accuracy

if __name__ == "__main__":
    typing_speedtest()
            