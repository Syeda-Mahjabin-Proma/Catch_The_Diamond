'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_AMD_performance_monitor'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_AMD_performance_monitor',error_checker=_errors._error_checker)
GL_COUNTER_RANGE_AMD=_C('GL_COUNTER_RANGE_AMD',0x8BC1)
GL_COUNTER_TYPE_AMD=_C('GL_COUNTER_TYPE_AMD',0x8BC0)
GL_PERCENTAGE_AMD=_C('GL_PERCENTAGE_AMD',0x8BC3)
GL_PERFMON_RESULT_AMD=_C('GL_PERFMON_RESULT_AMD',0x8BC6)
GL_PERFMON_RESULT_AVAILABLE_AMD=_C('GL_PERFMON_RESULT_AVAILABLE_AMD',0x8BC4)
GL_PERFMON_RESULT_SIZE_AMD=_C('GL_PERFMON_RESULT_SIZE_AMD',0x8BC5)
GL_UNSIGNED_INT64_AMD=_C('GL_UNSIGNED_INT64_AMD',0x8BC2)
@_f
@_p.types(None,_cs.GLuint)
def glBeginPerfMonitorAMD(monitor):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeletePerfMonitorsAMD(n,monitors):pass
@_f
@_p.types(None,_cs.GLuint)
def glEndPerfMonitorAMD(monitor):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenPerfMonitorsAMD(n,monitors):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray,arrays.GLintArray)
def glGetPerfMonitorCounterDataAMD(monitor,pname,dataSize,data,bytesWritten):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,ctypes.c_void_p)
def glGetPerfMonitorCounterInfoAMD(group,counter,pname,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetPerfMonitorCounterStringAMD(group,counter,bufSize,length,counterString):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray,arrays.GLintArray,_cs.GLsizei,arrays.GLuintArray)
def glGetPerfMonitorCountersAMD(group,numCounters,maxActiveCounters,counterSize,counters):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetPerfMonitorGroupStringAMD(group,bufSize,length,groupString):pass
@_f
@_p.types(None,arrays.GLintArray,_cs.GLsizei,arrays.GLuintArray)
def glGetPerfMonitorGroupsAMD(numGroups,groupsSize,groups):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLboolean,_cs.GLuint,_cs.GLint,arrays.GLuintArray)
def glSelectPerfMonitorCountersAMD(monitor,enable,group,numCounters,counterList):pass