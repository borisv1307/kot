import pydux


def counter(state, action):
    if state is None:
        state = 0
    if action is None:
        return state
    elif action['type'] == 'INCREMENT':
        return state + 1
    elif action['type'] == 'DECREMENT':
        return state - 1
    return state


# Create a Redux store holding the state of your app.
# Its API is { subscribe, dispatch, get_state }.
store = pydux.create_store(counter)

# You can use subscribe() to update the UI in response to state changes.
store.subscribe(lambda: print(store.get_state()))

# The only way to mutate the internal state is to dispatch an action.
# The actions can be serialized, logged or stored and later replayed.
store.dispatch({'type': 'INCREMENT'})
# 1
store.dispatch({'type': 'INCREMENT'})
# 2
store.dispatch({'type': 'DECREMENT'})
# 1
