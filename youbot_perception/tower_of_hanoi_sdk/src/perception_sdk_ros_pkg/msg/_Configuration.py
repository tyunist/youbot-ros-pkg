"""autogenerated by genmsg_py from Configuration.msg. Do not edit."""
import roslib.message
import struct


class Configuration(roslib.message.Message):
  _md5sum = "a6fb4fce26fb260d26b15c035aa9267e"
  _type = "perception_sdk_ros_pkg/Configuration"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#Indicates no of color-based regions to be searched for
uint32 no_of_regions
#Indicates number of maximum possible objects in each region
uint32 max_no_of_objects
#Indicates the HSV-Limits configuration filenames for all the regions separated by space
#For example: ./redRoiConfig.cfg
string config_files
#Indicates the labels for each region to be used for broadcasting the transforms for the objects
#separated by space 
#For example: red 
string labels
"""
  __slots__ = ['no_of_regions','max_no_of_objects','config_files','labels']
  _slot_types = ['uint32','uint32','string','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       no_of_regions,max_no_of_objects,config_files,labels
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(Configuration, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.no_of_regions is None:
        self.no_of_regions = 0
      if self.max_no_of_objects is None:
        self.max_no_of_objects = 0
      if self.config_files is None:
        self.config_files = ''
      if self.labels is None:
        self.labels = ''
    else:
      self.no_of_regions = 0
      self.max_no_of_objects = 0
      self.config_files = ''
      self.labels = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_2I.pack(_x.no_of_regions, _x.max_no_of_objects))
      _x = self.config_files
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.labels
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.no_of_regions, _x.max_no_of_objects,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.config_files = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.labels = str[start:end]
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_2I.pack(_x.no_of_regions, _x.max_no_of_objects))
      _x = self.config_files
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.labels
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.no_of_regions, _x.max_no_of_objects,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.config_files = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.labels = str[start:end]
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_2I = struct.Struct("<2I")
