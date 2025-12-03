import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\impar\Videos\TensorFlow\o.csv')
print(df)

# plt.scatter(df['km'], df["current price"])
# plt.show()


def loss_function(m , b , df) :         # using MSE

    totalloss=0
    for i in range(len(df)) :                # iterating over the whole dataset
        
        x = df['hours'].iloc[i]              # taking i/p -x
        y= df["scores"].iloc[i]
        y_pred = (m*x + b)                        # predicted_value for particular data point

        totalloss +=  (y - y_pred)**2          # mean squared error
    
    return totalloss/len(df)


def gradient_descent(m , b , df , learn_rate) :        # gradient -dirn ofsteepest(descent)_slope       

    msum , bsum = 0 , 0
    for i in range(len(df)) :

        x = df['hours'].iloc[i]              
        y= df["scores"].iloc[i]

        y_pred = (m*x + b )                       # predicting value for i/p as close to o/p as possible

        msum  +=  x*(y-y_pred) 
        bsum  +=  (y-y_pred)

    dm  = (-2/len(df) ) * msum                  # taken derivative w.r.t to m   - m_gradient
    db  = (-2/len(df) ) * bsum                # taken derivative w.r.t to b    -  b_gradient

    m_new = m - ( learn_rate * dm)
    b_new = b - ( learn_rate * db)

    return m_new , b_new

m=0
b=0
learn_rate = 0.0001        
epochs= 3000

for i in range(epochs) :
    m , b = gradient_descent(m , b , df , learn_rate)

print(f"m = {m} ,b = {b}")



plt.scatter(df['hours'], df["scores"], color="black", label="Actual Data")

x_min = df['hours'].min()
x_max = df['hours'].max()
x_line = range(int(x_min), int(x_max))

y_line = [m*x + b for x in x_line]

plt.plot(x_line, y_line, color="red", label="Regression Line")

plt.xlabel("hours")
plt.ylabel("scores")
plt.legend()
plt.show()

