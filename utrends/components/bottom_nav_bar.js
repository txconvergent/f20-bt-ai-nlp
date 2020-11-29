import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import { StyleSheet, Image } from 'react-native';

import { HomeScreen } from '../screens/home.js';
import { SearchScreen } from '../screens/search.js';
import { SavedScreen } from '../screens/saved.js';
import { ProfilePage } from '../screens/profile.js';
import { SettingsPage } from '../screens/settings.js';

import { navigationRef } from '../RootNavigation.js';

const Tab = createBottomTabNavigator();

export const BottomNavBar = () => {
    return (
        <NavigationContainer ref={navigationRef}>
            <Tab.Navigator tabBarOptions={{showLabel: false, style: {borderTopColor: 'transparent'}}}>
                
                <Tab.Screen 
                        name="Home" 
                        component={HomeScreen} 
                        options={{
                            tabBarIcon: () => (
                                <Image
                                    style={styles.navIcon}
                                    source={require('../assets/home_unpressed.png')              
                                }/>
                            ),
                    }} />

                <Tab.Screen 
                    name="Search" 
                    component={SearchScreen} 
                    options={{
                        tabBarIcon: () => (
                            <Image
                                style={styles.navIcon}
                                source={require('../assets/search_unpressed.png')              
                            }/>
                        ),
                    }} />

                <Tab.Screen 
                    name="Saved" 
                    component={SavedScreen} 
                    options={{
                        tabBarIcon: () => (
                            <Image
                                style={styles.navIcon}
                                source={require('../assets/saved_unpressed.png')              
                            }/>
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