import React from 'react';
import { StyleSheet, View, Image, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';

import * as RootNavigation from '../RootNavigation.js';

export function TopNavBar() {

    return (
        <View style={styles.topBarContainer}>
            <TouchableOpacity style={styles.navIconContainer} onPress={() => RootNavigation.navigate('Settings')} >
                <Image style={styles.navIcon} source={require('../assets/settings.png')}/>
            </TouchableOpacity>

            <View style={styles.navIconContainer}>
                <Image style={styles.logo} source={require('../assets/logo_blue.png')}/>
            </View>

            <TouchableOpacity style={styles.navIconContainer} onPress={() => RootNavigation.navigate('Profile')}>
                <Image style={styles.navIcon} source={require('../assets/profile.png')}/>
            </TouchableOpacity>
        </View>
    );
}

const styles = StyleSheet.create({
    topBarContainer: {
        height: "10%",
        justifyContent: 'center',
        backgroundColor: 'white',
        alignItems: 'stretch',
        flexDirection: 'row',
        paddingTop: 20,
    },

    navIconContainer: {
        flexDirection: 'row',
        justifyContent: 'center',
        width: "33%",
    },

    navIcon: {
        width: 35,
        height: 35,
    },

    logo: {
        width: 40,
        height: 40,
        justifyContent: 'center',
    }
});