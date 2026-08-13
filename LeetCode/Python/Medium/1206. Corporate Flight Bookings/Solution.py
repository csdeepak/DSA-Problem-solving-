class Solution(object):
    def corpFlightBookings(self, bookings, n):
        arr=[0]*(n+2)
        for i in range(len(bookings)):
            arr[bookings[i][0]]+=bookings[i][2]
            arr[(bookings[i][1])+1]-=(bookings[i][2])
        prefix=0   
        for i in range(len(arr)):
            arr[i]+=prefix
            prefix=arr[i]         
        
        return arr[1:n+1]