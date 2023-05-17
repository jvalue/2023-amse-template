from deutsche_bahn_api.message import Message
import pandas as pd


class PlanChange:
    """ This class represents changed train attributes. """

    def __init__(self) -> None:
        self.station_number = None
        self.stop_id = None
        self.next_stations = None
        self.passed_stations = None
        self.arrival = None
        self.departure = None
        self.platform = None

    def insert_into_db(self, db_engine, table_name):
        db_engine.execute(
            f"""
            INSERT INTO {table_name} VALUES (
                {self.station_number}, '{self.stop_id}', '{self.next_stations}', '{self.passed_stations}', 
                '{self.arrival}', '{self.departure}', '{self.platform}'
              )
            """
        )
        db_engine.commit()
    
    def info(self) -> pd.DataFrame:
        df = pd.DataFrame({
            "Station Number": self.station_number,
            "Stop ID": self.stop_id,
            "Passed Stations": self.passed_stations,
            "Next Stations": self.next_stations,
            "Arrival Time": self.arrival,
            "Departure Time": self.departure,
            "Platform": self.platform,
        }, index=[0])
        return df
