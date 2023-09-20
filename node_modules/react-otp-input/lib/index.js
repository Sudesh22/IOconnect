'use strict';

var React = require('react');

var isStyleObject = function (obj) { return typeof obj === 'object' && obj !== null; };
var OTPInput = function (_a) {
    var _b = _a.value, value = _b === void 0 ? '' : _b, _c = _a.numInputs, numInputs = _c === void 0 ? 4 : _c, onChange = _a.onChange, renderInput = _a.renderInput, _d = _a.shouldAutoFocus, shouldAutoFocus = _d === void 0 ? false : _d, _e = _a.inputType, inputType = _e === void 0 ? 'text' : _e, renderSeparator = _a.renderSeparator, placeholder = _a.placeholder, containerStyle = _a.containerStyle, inputStyle = _a.inputStyle;
    var _f = React.useState(0), activeInput = _f[0], setActiveInput = _f[1];
    var inputRefs = React.useRef([]);
    var getOTPValue = function () { return (value ? value.toString().split('') : []); };
    React.useEffect(function () {
        inputRefs.current = inputRefs.current.slice(0, numInputs);
    }, [numInputs]);
    React.useEffect(function () {
        var _a;
        if (shouldAutoFocus) {
            (_a = inputRefs.current[0]) === null || _a === void 0 ? void 0 : _a.focus();
        }
    }, [shouldAutoFocus]);
    var getPlaceholderValue = function () {
        if (typeof placeholder === 'string') {
            if (placeholder.length === numInputs) {
                return placeholder;
            }
            if (placeholder.length > 0) {
                console.error('Length of the placeholder should be equal to the number of inputs.');
            }
        }
        return undefined;
    };
    var isInputValueValid = function (value) {
        return typeof value === 'string' && value.trim().length === 1;
    };
    var handleChange = function (event) {
        var value = event.target.value;
        if (isInputValueValid(value)) {
            changeCodeAtFocus(value);
            focusInput(activeInput + 1);
        }
        else {
            var nativeEvent = event.nativeEvent;
            // @ts-expect-error - This was added previosly to handle and edge case
            // for dealing with keyCode "229 Unidentified" on Android. Check if this is
            // still needed.
            if (nativeEvent.data === null && nativeEvent.inputType === 'deleteContentBackward') {
                event.preventDefault();
                changeCodeAtFocus('');
                focusInput(activeInput - 1);
            }
        }
    };
    var handleFocus = function (event) { return function (index) {
        setActiveInput(index);
        event.target.select();
    }; };
    var handleBlur = function () {
        setActiveInput(activeInput - 1);
    };
    var handleKeyDown = function (event) {
        var otp = getOTPValue();
        if (event.code === 'Backspace') {
            event.preventDefault();
            changeCodeAtFocus('');
            focusInput(activeInput - 1);
        }
        else if (event.code === 'Delete') {
            event.preventDefault();
            changeCodeAtFocus('');
        }
        else if (event.code === 'ArrowLeft') {
            event.preventDefault();
            focusInput(activeInput - 1);
        }
        else if (event.code === 'ArrowRight') {
            event.preventDefault();
            focusInput(activeInput + 1);
        }
        // React does not trigger onChange when the same value is entered
        // again. So we need to focus the next input manually in this case.
        else if (event.key === otp[activeInput]) {
            event.preventDefault();
            focusInput(activeInput + 1);
        }
        else if (event.code === 'Spacebar' ||
            event.code === 'Space' ||
            event.code === 'ArrowUp' ||
            event.code === 'ArrowDown') {
            event.preventDefault();
        }
    };
    var focusInput = function (index) {
        var _a, _b;
        var activeInput = Math.max(Math.min(numInputs - 1, index), 0);
        if (inputRefs.current[activeInput]) {
            (_a = inputRefs.current[activeInput]) === null || _a === void 0 ? void 0 : _a.focus();
            (_b = inputRefs.current[activeInput]) === null || _b === void 0 ? void 0 : _b.select();
            setActiveInput(activeInput);
        }
    };
    var changeCodeAtFocus = function (value) {
        var otp = getOTPValue();
        otp[activeInput] = value[0];
        handleOTPChange(otp);
    };
    var handleOTPChange = function (otp) {
        var otpValue = otp.join('');
        onChange(otpValue);
    };
    var handlePaste = function (event) {
        var _a;
        event.preventDefault();
        var otp = getOTPValue();
        var nextActiveInput = activeInput;
        // Get pastedData in an array of max size (num of inputs - current position)
        var pastedData = event.clipboardData
            .getData('text/plain')
            .slice(0, numInputs - activeInput)
            .split('');
        // Prevent pasting if the clipboard data contains non-numeric values
        if (inputType === 'number' && pastedData.some(function (value) { return isNaN(Number(value)); })) {
            return;
        }
        // Paste data from focused input onwards
        for (var pos = 0; pos < numInputs; ++pos) {
            if (pos >= activeInput && pastedData.length > 0) {
                otp[pos] = (_a = pastedData.shift()) !== null && _a !== void 0 ? _a : '';
                nextActiveInput++;
            }
        }
        focusInput(nextActiveInput);
        handleOTPChange(otp);
    };
    return (React.createElement("div", { style: Object.assign({ display: 'flex', alignItems: 'center' }, isStyleObject(containerStyle) && containerStyle), className: typeof containerStyle === 'string' ? containerStyle : undefined }, Array.from({ length: numInputs }, function (_, index) { return index; }).map(function (index) {
        var _a, _b, _c;
        return (React.createElement(React.Fragment, { key: index },
            renderInput({
                value: (_a = getOTPValue()[index]) !== null && _a !== void 0 ? _a : '',
                placeholder: (_c = (_b = getPlaceholderValue()) === null || _b === void 0 ? void 0 : _b[index]) !== null && _c !== void 0 ? _c : undefined,
                ref: function (element) { return (inputRefs.current[index] = element); },
                onChange: handleChange,
                onFocus: function (event) { return handleFocus(event)(index); },
                onBlur: handleBlur,
                onKeyDown: handleKeyDown,
                onPaste: handlePaste,
                autoComplete: 'off',
                maxLength: 1,
                'aria-label': "Please enter OTP character ".concat(index + 1),
                style: Object.assign({ width: '1em', textAlign: 'center' }, isStyleObject(inputStyle) && inputStyle),
                className: typeof inputStyle === 'string' ? inputStyle : undefined,
                type: inputType,
            }, index),
            index < numInputs - 1 && (typeof renderSeparator === 'function' ? renderSeparator(index) : renderSeparator)));
    })));
};

module.exports = OTPInput;
//# sourceMappingURL=index.js.map
