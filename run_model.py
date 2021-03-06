from flask import Blueprint, jsonify, request
import constants as CONST
import pandas as pd
from helper_function import *

bp = Blueprint("api", __name__)
status='status'
data='data'
#----------------boarder ROUTES----------------------#



@bp.route("/get_all_boarders", methods=["GET"])
def get_all_boarders():
    try:  
        engine, connection = make_conn()
        boarder_meta=[]
        query = "SELECT * from boarder_details ;"
        df = pd.read_sql(query, engine)   #TO FETCH

        if len(df) < 1:    #Empty boarder Data (No boarders)
            connection.close()
            return ({status:'Success',data:[]})
        else:
            for index, rows in df.iterrows():
                obj = {
                    "rollNo": rows.rollNo,
                    "first_name": rows.first_name,
                    "last_name": rows.last_name,
                    "phoneNumber": rows.phoneNumber,
                    "department": rows.department,
                    "programme": rows.programme,
                    "email": rows.email,
                    "dateOfBirth": rows.dateOfBirth,
                    "address": rows.address,
                    "roomNo": rows.roomNo
                }
                boarder_meta.append(obj)
            connection.close()
            return ({status:'Success',data:boarder_meta})

    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/get_boarder", methods=["POST"])
def get_boarder():
    try:  
        engine, connection = make_conn()
        rollNo = str(request.json["rollNo"])
        query = "select * from boarder_details where rollNo = "+rollNo+" ;"
        df = pd.read_sql(query, engine)   #TO FETCH
        boarder_meta={}
        if len(df) < 1:    #Empty boarder Data (No boarder)
            ({status:'Success',data:{}})
        else:
            for index, rows in df.iterrows():
                boarder_meta = rows
            connection.close()
            return ({status:'Success',data:boarder_meta})

    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/add_boarders", methods=["POST"])
def add_profile():
    try:  
            engine, connection = make_conn()
            
            rollNo=str(request.json["rollNo"])
            first_name=str(request.json["first_name"])
            last_name=str(request.json["last_name"])
            phoneNumber=str(request.json["phoneNumber"])
            department=str(request.json["department"])
            programme=str(request.json["programme"])
            email=str(request.json["email"])
            dateOfBirth=str(request.json["dateOfBirth"])
            address=str(request.json["address"])
            roomNo=str(request.json["roomNo"])

            query="insert into boarder_details(rollNo,first_name,last_name,phoneNumber,department,programme,email,dateOfBirth,address,roomNo) values("+rollNo+","+first_name+","+last_name+","+phoneNumber+","+department+","+programme+","+email+","+dateOfBirth+","+address+","+roomNo+");"
            connection.execute(query)   #TO INSERT

            query="select (rollNo,first_name,last_name,phoneNumber,department,programme,email,dateOfBirth,address,roomNo) from boarder_details where rollNo = "+rollNo+" ;"
            df = pd.read_sql(query, engine)    #TO FETCH

            boarder_meta = {}
            for index, rows in df.iterrows():
                    boarder_meta = {
                        "rollNo": rows.rollNo,
                        "first_name": rows.first_name,
                        "last_name": rows.last_name,
                        "phoneNumber": rows.phoneNumber,
                        "department": rows.department,
                        "programme": rows.programme,
                        "email": rows.email,
                        "dateOfBirth": rows.dateOfBirth,
                        "address": rows.address,
                        "roomNo": rows.roomNo
                    }
            connection.close()
            return({status:'Success',data:boarder_meta})
    
    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/update_boarder", methods=["POST"])
def boarder_update():

    try:
        engine, connection = make_conn()
        rollNo=str(request.json["rollNo"])
        first_name=str(request.json["first_name"])
        last_name=str(request.json["last_name"])
        phoneNumber=str(request.json["phoneNumber"])
        department=str(request.json["department"])
        programme=str(request.json["programme"])
        email=str(request.json["email"])
        dateOfBirth=str(request.json["dateOfBirth"])
        address=str(request.json["address"])
        roomNo=str(request.json["roomNo"])
        updateString = "UPDATE boarder_details SET first_name = "+first_name+", last_name = "+last_name+", phoneNumber="+phoneNumber+",department="+department+",programme="+programme+",email="+email+",dateOfBirth="+dateOfBirth+",address="+address+",roomNo="+roomNo+" WHERE rollNo = "+rollNo+" ;"
        connection.execute(updateString)  #TO UPDATE

        query = "SELECT rollNo,first_name,last_name,phoneNumber,department,programme,email,dateOfBirth,address,roomNo from boarder_details where rollNo = "+rollNo+" ;"
        df = pd.read_sql(query, engine)

        boarder_meta = {}
        for index, rows in df.iterrows():
            boarder_meta = {
                    "rollNo": rows.rollNo,
                    "first_name": rows.first_name,
                    "last_name": rows.last_name,
                    "phoneNumber": rows.phoneNumber,
                    "department": rows.department,
                    "programme": rows.programme,
                    "email": rows.email,
                    "dateOfBirth": rows.dateOfBirth,
                    "address": rows.address,
                    "roomNo": rows.roomNo
            }

        connection.close()
        return({status:'Success',data:boarder_meta})

    except Exception as e:
        return ({status:'Failed',data:e})

#----------------rooms ROUTES----------------------#


@bp.route("/get_all_rooms", methods=["GET"])
def get_all_rooms():
    try:  
        engine, connection = make_conn()
        room_meta=[]
        query = "SELECT * from rooms ;"
        df = pd.read_sql(query, engine)   #TO FETCH

        if len(df) < 1:    #Empty room Data (No room)
            connection.close()
            return ({status:'Success',data:[]})
        else:
            for index, rows in df.iterrows():
                obj = {
                    "roomNo": rows.roomNo,
                    "floor": rows.floor
                }
                room_meta.append(obj)
            connection.close()
            return ({status:'Success',data:room_meta})

    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/get_room", methods=["POST"])
def get_room():
    try:  
        engine, connection = make_conn()
        roomNo = str(request.json["roomNo"])
        query = "select * from rooms where roomNo = "+roomNo+" ;"
        df = pd.read_sql(query, engine)   #TO FETCH
        room_meta={}
        if len(df) < 1:    #Empty room Data (No room)
            ({status:'Success',data:{}})
        else:
            for index, rows in df.iterrows():
                room_meta = rows
            connection.close()
            return ({status:'Success',data:room_meta})

    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/add_rooms", methods=["POST"])
def add_room():
    try:  
            engine, connection = make_conn()
            
            roomNo=str(request.json["roomNo"])
            floor=str(request.json["floor"])

            query="insert into rooms(roomNo,floor) values("+roomNo+","+floor+");"
            connection.execute(query)   #TO INSERT

            query="select (roomNo,floor) from rooms where roomNo = "+roomNo+" ;"
            df = pd.read_sql(query, engine)    #TO FETCH

            room_meta = {}
            for index, rows in df.iterrows():
                    room_meta = {
                        "roomNo": rows.roomNo,
                        "floor": rows.floor
                    }
            connection.close()
            return({status:'Success',data:room_meta})
    
    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/update_room", methods=["POST"])
def room_update():

    try:
        engine, connection = make_conn()
        roomNo=str(request.json["roomNo"])
        floor=str(request.json["floor"])

        updateString = "UPDATE rooms SET roomNo = "+roomNo+", floor = "+floor+" ;"
        connection.execute(updateString)  #TO UPDATE

        query = "SELECT (roomNo,floor) from rooms where roomNo = "+roomNo+" ;"
        df = pd.read_sql(query, engine)

        room_meta = {}
        for index, rows in df.iterrows():
            room_meta = {
                "roomNo": rows.roomNo,
                "floor": rows.floor
            }

        connection.close()
        return({status:'Success',data:room_meta})

    except Exception as e:
        return ({status:'Failed',data:e})

#----------------representatives ROUTES----------------------#


@bp.route("/get_all_representatives", methods=["GET"])
def get_all_representatives():
    try:  
        engine, connection = make_conn()
        representatives_meta=[]
        query = "SELECT * from representatives ;"
        df = pd.read_sql(query, engine)   #TO FETCH

        if len(df) < 1:    #Empty representatives Data
            connection.close()
            return ({status:'Success',data:[]})
        else:
            for index, rows in df.iterrows():
                obj = {
                    "role": rows.role,
                    "rollNo": rows.rollNo
                }
                representatives_meta.append(obj)
            connection.close()
            return ({status:'Success',data:representatives_meta})

    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/get_representative", methods=["POST"])
def get_representative():
    try:  
        engine, connection = make_conn()
        role = str(request.json["role"])
        query = "select * from representatives where role = "+role+" ;"
        df = pd.read_sql(query, engine)   #TO FETCH
        representatives_meta={}
        if len(df) < 1:    
            ({status:'Success',data:{}})
        else:
            for index, rows in df.iterrows():
                representatives_meta = rows
            connection.close()
            return ({status:'Success',data:representatives_meta})

    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/add_representatives", methods=["POST"])
def add_representatives():
    try:  
            engine, connection = make_conn()
            
            rollNo=str(request.json["rollNo"])
            role=str(request.json["role"])

            query="insert into representatives(role,rollNo) values("+role+","+rollNo+");"
            connection.execute(query)   #TO INSERT

            query="select (role,rollNo) from representatives where role = "+role+" ;"
            df = pd.read_sql(query, engine)    #TO FETCH

            representatives_meta = {}
            for index, rows in df.iterrows():
                    representatives_meta = {
                        "role": rows.role,
                        "rollNo": rows.rollNo
                    }
            connection.close()
            return({status:'Success',data:representatives_meta})
    
    except Exception as e:
        return ({status:'Failed',data:e})


@bp.route("/update_representatives", methods=["POST"])
def representatives_update():

    try:
        engine, connection = make_conn()
        rollNo=str(request.json["rollNo"])
        role=str(request.json["role"])

        updateString = "UPDATE rooms SET rollNo = "+rollNo+", role = "+role+" ;"
        connection.execute(updateString)  #TO UPDATE

        query ="select (role,rollNo) from representatives where role = "+role+" ;"
        df = pd.read_sql(query, engine)

        representatives_meta = {}
        for index, rows in df.iterrows():
            representatives_meta = {
                "role": rows.role,
                "rollNo": rows.rollNo
            }

        connection.close()
        return({status:'Success',data:representatives_meta})

    except Exception as e:
        return ({status:'Failed',data:e})
