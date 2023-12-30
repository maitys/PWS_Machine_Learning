# import multiprocessing
# def test():
#     print("this is my multiprocessing prog")

# if __name__ == "__main__":
#     m = multiprocessing.Process(target=test)
#     print("this is my main program")
#     m.start()
#     m.join()

###################################################################
# import multiprocessing
# def square(n):
#     return n**2
# if __name__ == '__main__':
#     with multiprocessing.Pool(processes=5) as pool :
#         out =pool.map(square , [3,4,5,6,6,7,87,8,8])
#         print(out)

###################################################################
# import multiprocessing
# def producer(q):
#     for i in ["sudh" , "kumar" , "pwskills" , "krish" ,"naik"] : 
#         q.put(i)
    
# def consume(q) : 
#     while True :
#         item = q.get()
#         if item is None :
#             break 
#         print(item)
        
# if __name__ == '__main__':
#     queue = multiprocessing.Queue()
#     m1 = multiprocessing.Process(target=producer , args= (queue,))
#     m2 = multiprocessing.Process(target=consume ,args=(queue,) )
#     m1.start()
#     m2.start()
#     queue.put("xyz")
#     m1.join()
#     m2.join()

###################################################################
# import multiprocessing
# def square(index , value ):
#     value[index] = value[index] **2
    
# if __name__ == '__main__':
#     arr = multiprocessing.Array('i', [2,3,6,7,8,8,9,3,3,3])
#     process = []
#     for i in range(10) : 
#         m = multiprocessing.Process(target=square , args = (i ,arr ))
#         process.append(m)
#         m.start()
#     for m in process:
#         m.join()
#     print(list(arr))

###################################################################
# import multiprocessing
# def sender(conn , msg):
#     for i in msg:
#         conn.send(i)
#     conn.close()
    
# def receive(conn) :
#     while True:
#         try:
#             msg = conn.recv()
#         except Exception as e :
#             print(e)
#             break
#         print(msg)

# if __name__ == '__main__':
#     msg = ["my name is sudh" , "this is my msg  to my students " , "i am taking class for dsm " , "try to practice all the code "]
#     parent_conn , child_conn = multiprocessing.Pipe()
#     m1 = multiprocessing.Process(target=sender , args = (child_conn , msg))
#     m2 = multiprocessing.Process(target=receive , args = (parent_conn,))
#     m1.start()
#     m2.start()
#     m1.join()
#     child_conn.close()
#     m2.join()
#     parent_conn.close()

###################################################################


    

