import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';

import { HomeScreen } from '../screens/home.js';
import { SearchScreen } from '../screens/search.js';
import { SavedScreen } from '../screens/saved.js';
import { ProfilePage } from '../screens/profile.js';
import { SettingsPage } from '../screens/settings.js';

const Tab = createBottomTabNavigator();

export const BottomNavBar = () => {
    return (
        <NavigationContainer>
            <Tab.Navigator>
                <Tab.Screen name="Home" component={HomeScreen} />
                <Tab.Screen name="Search" component={SearchScreen} />
                <Tab.Screen name="Saved" component={SavedScreen} />
                <Tab.Screen name="Profile" component={ProfilePage} options={{tabBarButton: () => null, tabBarVisible: false}} />
                <Tab.Screen name="Settings" component={SettingsPage} options={{tabBarButton: () => null, tabBarVisible: false}} />
            </Tab.Navigator>
        </NavigationContainer>
    );
}
