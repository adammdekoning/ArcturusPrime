import pandas as pd
import pyodbc
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arcturusPrime.settings')
import django
django.setup()
# from baseWebApp.models import Athlete, SeasonPeriod, ErgData
from frontEnd.models import Athlete, Club, Session_Data, Result, Distance_Data, Season_Period

conn = pyodbc.connect('driver={SQL Server};'
                        'Server=ADAMSXPS13\SQLEXPRESS;'
                        'Database=ADK_Initial;'
                        'Trusted_Connection=yes;')




# def getSeasonPeriod():
#     sql = 'select distinct(period) from ADK_Initial..CG_erg_data'
#
#     df = pd.DataFrame(pd.read_sql_query(sql, conn))
#     return df

def getErgData():
    sql = """select [name]
            ,[time]
            ,[season]
            ,[date]
            ,[period]
            ,[distance]
            ,[rate]
            FROM [ADK_Initial].[dbo].[CG_erg_data]
            """


    df = pd.DataFrame(pd.read_sql_query(sql, conn))
    df['rate'].fillna('-', inplace=True)
    return df


def populateErgData(df):
    r = 1
    for index, row in df.iterrows():

        entry = Result.objects.create(
        session = Session_Data.objects.get(date=row['date']),
        distance = row['distance'],
        time = row['time'],
        rate = row['rate'],
        )

        a = Athlete.objects.get(name=row['name'])

        entry.crew.add(a)

        print("{}, {}, {}".format(r, row['name'], row['date']))

        r += 1



def getAthletes():
    sql = 'select * from ADK_Initial..athlete_backup'

    df = pd.DataFrame(pd.read_sql_query(sql, conn))
    return df


def populateAthletes(df):

    for index, row in df.iterrows():

        entry = Athlete.objects.create(
                            name=row['name'],
                            year_seven_year=row['year_eight_season'],
                            club=Club.objects.get(name='Queenwood'))



def getSessionData():

    sql = """
    select distinct date FROM [ADK_Initial].[dbo].[CG_erg_data]
    """

    df = pd.DataFrame(pd.read_sql_query(sql, conn))

    return df


def populateSessionData(df):
    for index, row in df.iterrows():

        entry = Session_Data.objects.create(
        date = row['date'],
        type = 'erg',
        )

def getDistanceData():
    sql = """
    select * from [ADK_Initial].[dbo].[CG_data]
    """

    df = pd.DataFrame(pd.read_sql_query(sql, conn))
    df['rate'].fillna('-', inplace=True)
    # df['time'].fillna('-', inplace=True)
    # df['boat_type'].fillna('-', inplace=True)
    # df['notes'].fillna('-', inplace=True)

    return df

def populateDistanceData(df):
    r = 1
    for index, row in df.iterrows():
        entry = Distance_Data.objects.create(
        athlete = Athlete.objects.get(name=row['name']),
        date = row['date'],
        boat_class = row['boat_type'],
        distance = row['distance'],
        time = row['time'],
        rate = row['rate'],
        notes = row['notes'],
        type = row['sessionType']
        )
        print("{}: {}: {}".format(r, row['name'], row['date']))
        r += 1


def getSeasonPeriodData():

    sql = """ select * from [ADK_Initial].[dbo].[period_dates] """

    df = pd.DataFrame(pd.read_sql_query(sql, conn))
    df['period'] = df['period'].map(lambda x: str(x)[:-5])

    return df


def populateSeasonPeriodData(df):
    for index, row in df.iterrows():

        entry = Season_Period.objects.create(
        period = row['period'],
        season = row['season'],
        start_date = row['start_date'],
        end_date = row['end_date']
        )


if __name__=="__main__":
    print("beginning process...")
    # populateDistanceData(getDistanceData())
    populateSessionData(getSessionData())
    populateErgData(getErgData())
    print("process complete.")
