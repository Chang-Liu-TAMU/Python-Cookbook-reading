#using many conditional checks
class Connection:
    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('reading')

    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open')
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        self.state = 'CLOSED'


#delegate to the state class
class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
            self._state = newstate

    # Delegate to the state class
    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)

# Connection state base class
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()

# Implementation of different states
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')

class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')
    @staticmethod
    def write(conn, data):
        print('writing')
    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')
    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


#
# c = Connection()
# print(c._state)
# # c.read()
# c.open()
# print(c._state)
# c.read()
# c.write("hello")
# c.close()

"""
An alternative implementation technique concerns direct manipulation of the
__class__ attribute of instances.
"""
class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('Not open')
    def write(self, data):
        raise RuntimeError('Not open')
    def open(self):
        self.new_state(OpenConnection)
    def close(self):
        raise RuntimeError('Already closed')


class OpenConnection(Connection):
    def read(self):
        print('reading')

    def write(self, data):
        print('writing')

    def open(self):
        raise RuntimeError('Already open')

    def close(self):
        self.new_state(ClosedConnection)


c = Connection()
print(c)
c.open()
print(c)
c.close()
print(c)


#****************************** summary ************************************
# Original implementation
# class State:
#     def __init__(self):
#         self.state = 'A'
#     def action(self, x):
#         if state == 'A':
#             # Action for A
#             state = 'B'
#             pass
#         elif state == 'B':
#             # Action for B
#             state = 'C'
#             pass
#         elif state == 'C':
#             # Action for C
#             ...
#             state = 'A'


# Alternative implementation
# class State:
#     def __init__(self):
#         self.new_state(State_A)
#
#     def new_state(self, state):
#         self.__class__ = state
#
#     def action(self, x):
#         raise NotImplementedError()

# class State_A(State):
#     def action(self, x):
#         # Action for A
#         ...
#         self.new_state(State_B)

# class State_B(State):
#     def action(self, x):
#         # Action for B
#         ...
#         self.new_state(State_C)
#
# class State_C(State):
#     def action(self, x):
#         # Action for C
#         ...
#         self.new_state(State_A)