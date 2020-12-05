import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export const SettingsPage = () => {
    return (
        <View style={styles.container}>
          <Text>Settings</Text>
        </View>
      );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  }
});
