def read_csv(filename):
    data=[]
    with open(filename,"r") as f:
        for line in f:
            row=line.strip().split(",")
            data.append(row)
    return data

def FindS(data):
    hypo=None
    target=len(data[0])-1
    step=1
    for row in data:
        if row[target].lower()=="yes":
            if hypo==None:
                hypo=row[:-1]
                print(f"Step {step}:hypothesis={hypo}\n")
            else:
                for i in range(len(hypo)):
                    if(hypo[i]!=row[i]):
                        hypo[i]="?"
                print(f"Step {step}:hypothesis={hypo}\n")
            step+=1
        else:
            print("skipping negative example\n")
    
    print(f"Final hypothesis={hypo}\n")


if __name__=="__main__":
    data=read_csv("training.csv");
    FindS(data)


        
            
