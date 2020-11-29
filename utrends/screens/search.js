import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export function SearchScreen() {
    return (
      <View style={styles.container}>
        <Text>Search</Text>
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