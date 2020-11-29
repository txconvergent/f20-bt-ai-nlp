import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import { StyleSheet, Image } from 'react-native';

import { SwipeScreen } from '../screens/home.js';
import { SearchScreen } from '../screens/search.js';
import { SavedScreen } from '../screens/saved.js';
import { ProfilePage } from '../screens/profile.js';
import { SettingsPage } from '../screens/settings.js';

import { navigationRef } from '../RootNavigation.js';

const Tab = createBottomTabNavigator();

const images = {
    home: {
        unpressed: require('../assets/home_unpressed.png'),
        pressed: require('../assets/home_pressed.png'),
    },

    search: {
        unpressed: require('../assets/search_unpressed.png'),
        pressed: require('../assets/search_pressed.png'),
    },

    saved: {
        unpressed: require('../assets/saved_unpressed.png'),
        pressed: require('../assets/saved_pressed.png'),
    },
}

export const BottomNavBar = () => {
    return (
        <NavigationContainer ref={navigationRef}>
            <Tab.Navigator tabBarOptions={{showLabel: false, style: {borderTopColor: 'transparent'}}}>
                
                <Tab.Screen 
                        name="Home" 
                        component={SwipeScreen} 
                        options={{
                            tabBarIcon: ({focused}) => (
                                <Image
                                    style={styles.navIcon}
                                    source={focused ? images.home.pressed : images.home.unpressed}          
                                />
                            ),
                    }} />

                <Tab.Screen 
                    name="Search" 
                    component={SearchScreen} 
                    options={{
                        tabBarIcon: ({focused}) => (
                            <Image
                                style={styles.navIcon}
                                source={focused ? images.search.pressed : images.search.unpressed}       
                            />
                        ),
                    }} />

                <Tab.Screen 
                    name="Saved" 
                    component={SavedScreen} 
                    options={{
                        tabBarIcon: ({focused}) => (
                            <Image
                                style={styles.navIcon}
                                source={focused ? images.saved.pressed : images.saved.unpressed}       
                            />
                        ),
                    }} />


                <Tab.Screen name="Profile" component={ProfilePage} options={{tabBarButton: () => null, tabBarVisible: true}} />
                <Tab.Screen name="Settings" component={SettingsPage} options={{tabBarButton: () => null, tabBarVisible: true}} />
            </Tab.Navigator>
        </NavigationContainer>
    );
}

const styles = StyleSheet.create({
    navIcon: {
        width: 55,
        height: 55,
    }
});