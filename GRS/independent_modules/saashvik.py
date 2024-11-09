def format_config(config):

    def isvar(component):
        if len(component) <= 1:
            return False
        if '=' in component:
            if component.replace(' ', '')[len(component.replace(' ', ''))-1] == ';':
                return True
            else:
                rep = ''
                for char in component:
                    if char != ' ':
                        if char == '=':
                            if '=' in rep:
                                return False
                            else:
                                rep += '='
                        elif not len(rep):
                            rep += 'v'
                        elif rep[len(rep)-1] == '=':
                            rep += 't'
                    elif rep[len(rep)-1] == ',':
                        continue
                    else:
                        rep += ' '
                if rep.replace(',', '') == 'v=t':
                    return True
                    
        return False

    index = 0
    components = []
    component = ''
    for char in config:
        component += char
        if char == '\n' or char == ';':
            if '\n' in component and '=' in component:
                components.append(component.replace('\n', ''))
                component = '\n'
            components.append(component)
            component = ''
        index += 1
    
    for component in components:
        if isvar(component):
            index = components.index(component)
            component = component.replace(' ', '').replace('=', ' = ').replace(',', ', ')
            if component[len(component)-1] != ';':
                component += ';'
            components[index] = component
            
            
    config = ''
    for component in components:
        config += component

    return config

def parse_var(var_name, config=';'):
    config = config.replace(' ', '')
    var_name += '='
    if var_name in config:
        start_index = config.index(var_name) + len(var_name)
        end_index = config.index(';', start_index)
        if '\n' in config[start_index:end_index]:
            config = config.replace(var_name + '\n', '')
            var = parse_var(var_name, config)
            if var:
                return var
            else:
                return None
        else:
            return config[start_index:end_index]
    else:
        return None

def parse_csv_var(var_name, config=';'):
    config = config.replace(' ', '')
    var_name += '='
    if var_name in config:
        start_index = config.index(var_name) + len(var_name)
        end_index = config.index(';', start_index)
        if '\n' in config[start_index:end_index]:
            config = config.replace(var_name + '\n', '')
            var = parse_var(var_name, config)
            if var:
                return var.split(',')
            else:
                return None
        else:
            return config[start_index:end_index].split(',')
    else:
        return None