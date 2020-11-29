import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import { BottomNavBar } from './components/bottom_nav_bar.js';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <BottomNavBar/>
  );
}

const styles = StyleSheet.create({
  
});
