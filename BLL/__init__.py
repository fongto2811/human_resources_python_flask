from DTO import UserDTO
from DAL import UserDAL
from BLL.user import UserBLL

user_bll = UserBLL(UserDTO, UserDAL)