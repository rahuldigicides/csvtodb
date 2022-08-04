
from pydantic import BaseModel

# ! =========================     1. User Sechamas ===============================


class Userdata(BaseModel):
    userid: str
    password: str
    email: str
    role: str
    status: str
    company: str
    reporting: str
    blocked: int
    deleted: int
    phone: str
    name: str


class Userlogin(BaseModel):
    username: str
    password: str


class Userup(BaseModel):
    userid: str
    newvalue: int


class Userextra(BaseModel):
    userid: str
    usercol: str
    colvalue: str


class Myuser(BaseModel):
    userid: str


# !========================== 2. Global ROLES ============================
class Myglobalroles(BaseModel):
    roleid: str
    role: str


# ! ========================== 3. COMPANY ====================================

class Mycompany(BaseModel):
    companyid: str
    cname: str

# ! ========================== 4. COMPANY ROLES ====================================


class Mycompanyroles(BaseModel):
    roleid: str
    role: str
    description: str
    report_to: str
    company: str
    companyid: str


# ! ============= 5. APP FEATURES ========
class Myappfeatures(BaseModel):
    featureid: str
    featurename: str


# ! ================ 6. ROLE FEATURES =================
class Myrolefeatures(BaseModel):
    rfid: str
    featurename: str
    fid: str
    rolename: str
    rid: str
    readf: int
    writef: int


#!========================== 7 CSV FARMER ============================
class Farmercsv(BaseModel):
    id: str
    name: str
    updatedon: str
    updatedby: str
    status: str
    records: int
    errors: int
    importtype: str

#!========================== 8 MISSED CALL CAMPAIGN============================
class Missedcall(BaseModel):
    id: str
    name: str
    date: str
    starttime: str
    endtime: str
    agentname: str
    runtime: int
    createdby: str
    company_id: str


#!========================== 9 MISSED USER PROP============================
class Misseduserprops(BaseModel):
    id: str
    campaign_id: str
    propname: str
    propvalue: str

