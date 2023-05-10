class EventRegister():
    
    default_path = "sql.txt"

    def __init__(self, id: str, file_name: str = default_path):
        self.file_name: str  = file_name

    def formater(self, date: str, hour: str, server: str, event_type: str, description: str):
        return (date,hour,server,event_type,description)


    def save_data(self, element: str, path: str = default_path):
        element = str(element)+'\n'
        with open(path, 'a', encoding = 'utf-8') as info:
            info.write(element)
            pass

    def removing_invalid_characters(self, data: list):
        if isinstance(data, list):
            for i in range(0, len(data)):
                data[i] = data[i][:-1]
            return data
        return data

    def read_data(self, path: str = default_path):
        with open(path, 'r+', encoding = 'utf-8') as info:

            return self.removing_invalid_characters(info.readlines())

    def event_information(self, data: list):
        total_events = 0

        #TEMPORAL DATA
        list_event_type = []
        list_event_server = []

        #Total events
        for i in range(len(data)):
            data[i] = tuple(data[i])
        
        total_events = len(data)

        for index in data:
            #Event server
            if not (index[2] in list_event_server):
                list_event_server.append(index[2])
            if not (index[3] in list_event_type):
                list_event_type.append(index[2])
                pass

        total_events_server = len(list_event_server)
        total_events_type = len(list_event_type)

        return {'eventos totales': total_events,
                'eventos por server': total_events_server,
                'eventos por tipo': total_events_type
        }



logger = EventRegister("sql.txt")
data = logger.read_data()

print(logger.event_information(data))
