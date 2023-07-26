def add_meeting():
        start_time = 11
        end_time =  12
        # meeting_date = start_time.date()

        array = [[3, 4], [6, 7], [9, 11]]
        start, end = 0, len(array) - 1

        while(start <= end):
            mid = start + (end - start) // 2
            print(mid)
            mid_start_time, mid_end_time = array[mid][0], array[mid][1]

            if(end_time <= mid_start_time):
                end = mid - 1
            elif(start_time >= mid_end_time):
                start = mid + 1
            else:
                raise Exception("Overlapping Meetings encountered")
        
        array.insert(4, [11, 12])
        print(array)

        return end + 1 if end >=0 else 0 

if __name__ == '__main__':
    print(f"ANS : {add_meeting()}")