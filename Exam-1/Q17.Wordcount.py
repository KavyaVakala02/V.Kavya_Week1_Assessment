def get_input():
    sentences=input("enter sentences")
    return sentences
def counter(sentences):
    words = sentences.split()
# Create a dictionary to store word counts
    count = {}
    for word in words:  #looping to count words
        word = word.lower()  # Convert to lowercase 
        if word in count:
            count[word] += 1   #incrementing
        else:
            count[word] = 1
    return count
def main():
    sentences = input("Enter a sentence: ") # taking input
    count = counter(sentences)
    for word, count in count.items():
        print(f"'{word}': {count}")
main()