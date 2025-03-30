from random import *
class batsman:
    
    scores_list=[]
    total_runs=0
    max_score=0
    avg=0
    conunt_of_fifties=0
    conunt_of_hundereds=0
    
    def __init__(self,batter_name,batter_country,no_of_matches=None):
        self.name=batter_name
        self.country=batter_country
        if no_of_matches!=None:
            if no_of_matches<=95:
                self.no_of_matches=no_of_matches
            else:
                print("Invalid Number of Matches")
        else:
            x=randint(1,95)
            self.no_of_matches=x
        
    @property
    def name(self):
        return self.batter_name
    @name.setter
    def name(self,d):
        self.batter_name=d
        return

    @property
    def country(self):
        return self.batter_country
    @country.setter
    def country(self,d):
        self.batter_country=d
        return


    def score_list_maker(self):
        self.scores_list=[]
        for i in range(self.no_of_matches):
           score=randint(0,180)
           self.scores_list.append(score)
    
    def calcTotal(self):
        for i in range(len(self.scores_list)):
            self.total_runs+=self.scores_list[i]

    def calcAvg(self):
       self.avg=self.total_runs/self.no_of_matches

    def findmaxscore(self):
        for i in range(len(self.scores_list)):
            if self.scores_list[i]>self.max_score:
                self.max_score=self.scores_list[i]

    def count_fifties(self):
        for i in range(len(self.scores_list)):
            if self.scores_list[i]>=50:
                self.conunt_of_fifties+=1

    def count_hundereds(self):
        for i in range(len(self.scores_list)):
            if self.scores_list[i]>=100:
               self.conunt_of_hundereds+=1

    def show_stats(self):
        print("Batsman Name: ",self.batter_name)
        print("Batsman Country: ",self.batter_country)
        print("Batsman's Number of Matches: ",self.no_of_matches)
        print("Batsman Scores: ",self.scores_list)
        print("Batsman Total Runs Scored: ",self.total_runs)
        print("Batsman Average: ",self.avg)
        print("Batsman Highest Score: ",self.max_score)
        print("Batsman Total fifties: ",self.conunt_of_fifties)
        print("Batsman Total Hundreds: ",self.conunt_of_hundereds)
        
      
def main():
    batsman_list=[]
    batsman1=batsman("Babar Azam","Pakistan")
    batsman2=batsman("Kane Williamson","New Zealand",40)
    batsman3=batsman("Ben Strokes","England",88)
    
    
    batsman1.score_list_maker()
    batsman1.calcTotal()
    batsman1.calcAvg()
    batsman1.findmaxscore()
    batsman1.count_fifties()
    batsman1.count_hundereds()
    batsman_list.append(batsman1)
    
    batsman2.score_list_maker()
    batsman2.calcTotal()
    batsman2.calcAvg()
    batsman2.findmaxscore()
    batsman2.count_fifties()
    batsman2.count_hundereds()
    batsman_list.append(batsman2)

    batsman3.score_list_maker()
    batsman3.calcTotal()
    batsman2.calcAvg()
    batsman3.findmaxscore()
    batsman3.count_fifties()
    batsman3.count_hundereds()
    batsman_list.append(batsman3)

    for i in range(len(batsman_list)):
        batsman_list[i].show_stats()
        print()
           
main()


    
    
    
