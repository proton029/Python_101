attempt=0
score=0
while(attempt<4):
    actorName=input('Actor name:')
    if(actorName=='Roger Moore'):
        print('Well done: Roger Moore was Bond in Live and Let Die.')
        score+=1
    elif(actorName=='seanconnery'):
        print('Well done: Sean Connery was Bond in From Russia with Love.')
        score += 1
    elif (actorName == 'Pierce Brosnan'):
        print('Well done: Pierce Brosnan was Bond in Die Another Day')
        score += 1
    elif (actorName == 'Daniel Craig'):
        print('Well done: Daniel Craig was Bond in Skyfall')
        score += 1
    else:
        print(f'Sorry. {actorName} hasn’t played Bond as far as I know.')
    attempt+=1
print(f'Your score is {score} out of 4')

