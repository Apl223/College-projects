def convert(fromUnit, toUnit, value): 
    value = float(value)

    if fromUnit == toUnit:
        value = value
        return value

    if fromUnit == 'celsius':
        if toUnit == 'kelvin':
            value = value + 273.15
            return value

        elif toUnit == 'fahrenheit':
            value = value * 9/5 + 32
            return value
        else:
            raise ConversionsNotPossible('wrong unit')
    if fromUnit == 'fahrenheit':
        if toUnit == 'celsius':
            value = (value - 32) * 5/9
            return value
        elif toUnit == 'kelvin':
            value = (value + 459.67) * 5/9
            return value
        else:
            raise ConversionsNotPossible('wrong unit')
    if fromUnit == 'kelvin':
        if toUnit == 'celsius':
            value = value - 273.15
            return value
        elif toUnit == 'fahrenheit':
            value = value * 9/5 - 459.67
            return value
        else:
            raise ConversionsNotPossible('wrong unit')
                                        
    if fromUnit == 'miles':
        if toUnit == 'yards':
            value = value * 1760.0
            return value
        elif toUnit == 'meters':
            value = value * 1604.344
            return value
        else:
            raise ConversionsNotPossible('wrong unit')
                                        
    if fromUnit == 'yards':
        if toUnit == 'meters':
            value = value * 0.9144
            return value
        elif toUnit == 'miles':
            value = value/1760.0
            return value
        else:
            raise ConversionsNotPossible('wrong unit')
                                       
    if fromUnit == 'meters':
        if toUnit == 'miles':
            value = value * 0.000621
            return value
        elif toUnit == 'yards':
            value = value * 1.0936
            return value
        else:
            raise ConversionsNotPossible('wrong unit')

                                       