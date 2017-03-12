# coding=utf-8
from faker import Factory
import pandas as pd
import random
import numpy as np
fake = Factory.create()

def createNames(n):
    names = []
    for _ in range(0,n):
        names.append(str(fake.name()))
    return names
def createProfile(n):
    customer = []
    for _ in range(0,n):
        customer.append(fake.profile(fields=None, sex=None))
    return customer
def cc(n):
    cc = []
    for _ in range(0, n):
        cc.append(fake.credit_card_number(card_type=None))
    return cc

def location(n):
    loc = []
    for _ in range(0, n):
        loc.append(str(fake.secondary_address()))
    return loc
def locName(n):
    name = []
    for _ in range(0, n):
        name.append(str(fake.city()))
    return name

def createSize(n):
    s=[]
    for _ in range(0,n):
        s.append((fake.random_int(min=4000, max=9999)))
    return s

def createGreenroom(n):
    s=[]
    for _ in range(0,n):
        s.append((fake.random_int(min=1, max=10)))
    return s

def createShow(n):
    name = []
    for _ in range(0, n):
        name.append(str(fake.city()))
    return name

def createDate(n):
    s=[]
    for _ in range(0,n):
        s.append((fake.random_int(min=1990, max=2017)))
    return s

def createRandomDate(n,start_date,end_date):
    s = []
    date_range = pd.date_range(start_date,end_date)
    for _ in range(0,n):
        x = random.choice(date_range)
        s.append(x.to_datetime().date())
    return s

def createRandomTime(n,startTime,endTime):
    s = []
    date_range = pd.date_range(startTime,endTime,freq='1min')
    for _ in range(0,n):
        x = random.choice(date_range)
        s.append(x.to_datetime().time())
    return s

def createTickets(n):
    s = []
    for _ in range(0,n):
        s.append((fake.random_int(min = 1, max = 10)))
    return s
    
def generateCustomerCSV(n):
    a = createProfile(n)
    credit = cc(n)
    df = pd.DataFrame(a)
    df['payment_details'] = credit
    ids=[]
    for _ in range(1,n+1):
        ids.append(_)
    df['customer_id'] = ids
    customer = pd.DataFrame()
    customer = df[['customer_id','name','ssn','mail','payment_details']]
    customer = customer.rename(columns={"ssn": "phone_no", "mail": "email_id"})
    print ('Generating customer')
    customer.to_csv('customer.csv', sep = ',', quotechar='"',index=False)

def generateHallCSV(n):
    df = pd.DataFrame()
    ids=[]
    capacity =[]
    availability_label =[]
    for _ in range(1,n+1):
        ids.append(_)
        capacity.append(100)
        availability_label.append('YES')
    df['hall_id'] = ids
    df['capacity'] = capacity
    df['availability_label']=availability_label
    l = location(n)
    n = locName((n))
    df['location'] = l
    df['name_hall'] = n
    print ('Generating Hall')
    df.to_csv('hall.csv', sep = ',', quotechar='"',index=False)

def generateScreenCSV(n):
    df = pd.DataFrame()
    ids=[]
    s = createSize(n)
    type =[]
    experience =[]
    t=['Dome','Flat','Curve']
    e= ['2D','3D','4D']
    for _ in range(1,n+1):
        ids.append(_)
        type.append(random.choice(t))
        experience.append(random.choice(e))
    df['hall_id'] = ids
    df['size'] = s
    df['type']= type
    df['experience'] = experience
    print ('Generating Screen')
    df.to_csv('screen.csv', sep = ',', quotechar='"',index=False)

def generateAuditoriumCSV(n):
    df = pd.DataFrame()
    ids=[]
    s = createSize(n)
    greenrooms = createGreenroom(n)
    for _ in range(n+1,1001):
        ids.append(_)

    df['hall_id'] = ids
    df['stage_size'] = s
    df['no_of_green_rooms'] = greenrooms
    print ('Generating Auditorium')
    df.to_csv('auditorium.csv', sep = ',', quotechar='"',index=False)

def generateShowCSV(n):
    df = pd.DataFrame()
    ids=[]
    s = createShow(n)

    for _ in range(1,n+1):
        ids.append(_)

    df['show_id'] = ids
    df['show_name'] = s

    print ('Generating Shows')
    df.to_csv('shows.csv', sep = ',', quotechar='"',index=False)

def generatePerformancesCSV(n):
    df = pd.DataFrame()
    ids = []
    performers = createNames(n)
    performance_type =[]
    p = ['Play', 'Drama', 'Opera','Dance', 'Magic Show']
    for _ in range(n+1, 1001):
        ids.append(_)
        performance_type.append(random.choice(p))
    df['show_id'] = ids

    df['performers'] = performers
    df['performance_type'] = performance_type
    print('Generating Performances')
    df.to_csv('performances.csv', sep=',', quotechar='"', index=False)

def generateMoviesCSV(n):
    df = pd.DataFrame()
    ids = []
    cast = createNames(n)

    releaseDate = createDate(n)
    director = createNames(n)
    rating =[]
    r = ['R', 'PG-13', 'A','U', 'PG-16']
    for _ in range(1, n+1):
        ids.append(_)
        rating.append(random.choice(r))
    df['show_id'] = ids
    df['movie_cast'] = cast
    df['release_date'] = releaseDate
    df['director'] = director
    df['rating'] = rating
    print('Generating Movies')
    df.to_csv('movies.csv', sep=',', quotechar='"', index=False)

def generateReservationCSV(n):
    df = pd.DataFrame()
    ids = []
    show_id = []
    hall_id =[]
    
    movies_table = pd.read_csv('movies.csv')
    performance_table = pd.read_csv('performances.csv') 
    screen_table = pd.read_csv('screen.csv')
    auditorium_table = pd.read_csv('auditorium.csv')
    
    r_date = createRandomDate(n,'8/1/2016','12/31/2016')
    r_time = createRandomTime(n,'00:00','23:59')
    
    for _ in range(1,(n/2)+1):
        ids.append(_)
        show_id.append(random.choice(movies_table.show_id))
        hall_id.append(random.choice(screen_table.hall_id))
    for _ in range((n/2)+1,n+1):
        ids.append(_)
        show_id.append(random.choice(performance_table.show_id))
        hall_id.append(random.choice(auditorium_table.hall_id))
        
    df['r_id'] = ids 
    df['show_id'] = show_id
    df['hall_id'] = hall_id
    df['r_date'] = r_date
    df['r_time'] = r_time    
    
    print('Generating Reservation')
    df.to_csv('reservation.csv', sep=',', quotechar='"', index=False)

def generateEventTable(n):
    df = pd.DataFrame()    
    ids = []
    show_id = []
    time_event = []
    ticket_price = []
    
    reservation_table = pd.read_csv('reservation.csv')
    
    date_event = createRandomDate(n,'8/1/2017','12/31/2017')    
    t = ['09:00:00','12:00:00','15:00:00','18:00:00','21:00:00']
    r = [20,25,30,35,40,45,50]
    
    for _ in range(1,n+1):
        ids.append(_)
        ticket_price.append(random.choice(r))
        time_event.append(random.choice(t))
        show_id.append(random.choice(reservation_table.show_id))
                     
    df['e_id'] = ids
    df['show_id'] = show_id
    df['time_event'] = time_event
    df['date_event'] = date_event
    df['ticket_price'] = ticket_price
    
    # Implement constrait of no 2 shows reserved in same hall air on same date and time
    df.show_id.drop_duplicates()
    print('Generating EventTable')
    df.to_csv('eventTable.csv', sep=',', quotechar='"', index=False)

def generateBookingTable(n):
    df = pd.DataFrame()
    ids = []
    e_id = []
    customer_id = []
    num_tickets = createTickets(n)
    price = []
    booking_label = []
    
    event_table = pd.read_csv('eventTable.csv')
    customer_table = pd.read_csv('customer.csv')
    
    booking_date = createRandomDate(n,'1/1/2017','7/31/2017')
    booking_time = createRandomTime(n,'00:00','23:59')
    
    for _ in range(1,n+1):
        ids.append(_)
        booking_label.append('YES')
        customer_id.append(random.choice(customer_table.customer_id))
        s = random.choice(event_table.e_id)   
        e_id.append(s)                 
        price.append((event_table.ticket_price.loc[s]).astype(int) * num_tickets[_-1])
             
    df['booking_id'] = ids
    df['e_id'] = e_id
    df['customer_id'] = customer_id    
    df['num_tickets'] = num_tickets
    df['price'] = price
    df['booking_date'] = booking_date
    df['booking_time'] = booking_time
    df['booking_label'] = booking_label       
    print ('Generating Booking Table')
    df.to_csv('booking.csv', sep=',', quotechar='"', index=False)
    
def megacreate():
     #generateCustomerCSV(1000)
     #generateHallCSV(1000)
     #generateScreenCSV(500)
     #generateAuditoriumCSV(500)
     #generateShowCSV(1000)
     #generatePerformancesCSV(500)
     #generateMoviesCSV(500)
     generateReservationCSV(2000)
     generateEventTable(2000)
     generateBookingTable(3000)


megacreate()

