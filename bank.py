class Account:
      def __init__(self,name,number,password):
             self.name=name
             self.number=number
             self.password=password
             self.balance=0.0

      def deposit(self,deposit):
    
          if deposit<0:
              return "The amount has to be greater than zero"
          else:
            self.balance+=deposit
         
          return "Your have deposited {}.Your new your account balance  is  {}.".format(deposit,self.balance)
      def save(self,savings):
           self.savings=0.0
           return "I saved up {} yesterday,my new savings account balance is {}.".format(savings,self.savings)
      
      def withdrawal(self,amount):
          if amount<0:
              
              return "The amount must be greater than zero"
          elif amount>self.balance:
              return "You have insufficient funds to complete this request"

          else:
              self.balance-=amount
          return "You have withdrawn {}.Your new balance is: {}.".format(amount,self.balance)

      def borrow(self,loan):
          limit=15000
          amount=loan +self.balance
    
          if loan >limit:
              return "The loan is too high.Your loan limit is {}.Kindly borrow a lower amount".format(limit)
          elif loan<=limit and self.balance<0:
               return "You have an existing loan.Please pay up to get another one"
          elif loan<=limit and self.balance>0:
              loan_balance=loan+15/100*loan
              return "You have borrowed {} successfully.Your new account balance is {}.You new loan balance is :{}".format(loan,amount,loan_balance)
          else:
              return "The service you need is not available now.Please try again later."