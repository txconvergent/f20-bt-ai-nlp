import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import { StyleSheet, View, Text } from 'react-native';

const Stack = createStackNavigator();

export const TopNavBar = () => {
    return (
        <View style={styles.topBarContainer}>
            <Text>Hello</Text>
            <Text>Hello 2</Text>
            <Text>Hello 3</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    topBarContainer: {
        height: "10%",
        justifyContent: 'center',
        backgroundColor: 'red',
        flexDirection: 'row',
    },
});