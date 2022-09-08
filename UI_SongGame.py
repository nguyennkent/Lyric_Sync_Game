import requests

class UISongGame:

    def __init__(self):
        self.game = self.getGameObject()

    def getGameObject(self):
        search = "http://localhost:5000/testgame"
        response = requests.get(search)
        return response.json()

    def play(self):
        print("Guess the Billboard Top Songs by each Artist!")
        count = 1
        score = 0
        for i in self.game["items"]:
            print("Question " + str(count))

            print("https://www.youtube.com/watch?v=" + i["id"])

            result = input("Guess the song: ")
            answer = i["artist"] + " - " + i["title"]

            if result == answer :
                score += 1
                print("Good Job!")
            
            else:
                print("Wrong Answer!")
            
            print("The correct answer was: " + answer)
            count += 1

        print("Your score was: " + str(score) + "/" + str(len(self.game["items"])))
        
if __name__ == "__main__":
    x = UISongGame()
    x.play()