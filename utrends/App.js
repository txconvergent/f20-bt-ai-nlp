import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import { ProfilePage } from './screens/profile.js';
import { SettingsPage } from './screens/settings.js';
import { HomeScreen } from './screens/home.js';
import { SearchScreen } from './screens/search.js';
import { SavedScreen } from './screens/saved.js';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <>
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Home" component={HomeScreen} />
        <Tab.Screen name="Search" component={SearchScreen} />
        <Tab.Screen name="Saved" component={SavedScreen} />
        <Tab.Screen name="Profile" component={ProfilePage} />
        <Tab.Screen name="Settings" component={SettingsPage} />
      </Tab.Navigator>
    </NavigationContainer>
    </>
  );
}

const styles = StyleSheet.create({
  
});
